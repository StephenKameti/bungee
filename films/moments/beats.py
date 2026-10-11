"""beats.py: measure a track and write beats.json {bpm, beats, downbeats, hits, duration}.
Uses librosa when installed (best for supplied tracks); numpy fallback otherwise.
Usage: python3 beats.py audio/music.wav beats.json [--bpm 120] [--phase 0]
  Synthesized score: pin both (--bpm 120 --phase 0) so the grid is exact; the measurement still reports hits.
  Supplied track: pass nothing, or only --bpm if you know it. Downbeats are an estimate: listen, and if bar 1
  starts on another beat, rerun with --downbeat 0..3 (index of the first downbeat in the beat list).
"""
import json, sys, wave
import numpy as np

def load(path):
    try:
        import librosa
        y, sr = librosa.load(path, sr=22050, mono=True); return y, sr
    except ImportError:
        with wave.open(path) as w:
            sr, ch = w.getframerate(), w.getnchannels()
            y = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
        return y.reshape(-1, ch).mean(1), sr

def onset_env(y, sr, hop=512, n=2048, fmax=None):
    win = np.hanning(n); frames = 1 + (len(y) - n) // hop
    S = np.abs(np.stack([np.fft.rfft(win * y[i * hop:i * hop + n]) for i in range(frames)]))
    if fmax: S = S[:, : int(fmax / (sr / n)) + 1]  # low band = kick and bass: the pulse, not the shakers
    flux = np.maximum(0, np.diff(np.log1p(10 * S), axis=0)).sum(1)
    flux = np.concatenate([[0], flux])
    shift = int(round((n / 2) / hop))  # frame time = window centre
    flux = np.concatenate([np.zeros(shift), flux])[: len(flux)]
    return flux / (flux.max() + 1e-9), hop / sr

def main():
    src, dst = sys.argv[1], sys.argv[2]
    opt = lambda k: float(sys.argv[sys.argv.index(k) + 1]) if k in sys.argv else None
    pin, phase = opt("--bpm"), opt("--phase")
    y, sr = load(src); dur = len(y) / sr
    oenv, dt = onset_env(y, sr)
    low, _ = onset_env(y, sr, fmax=160)
    try:
        import librosa
        tempo, bt = librosa.beat.beat_track(y=y, sr=sr, start_bpm=pin or 120, units="time")
        bpm = float(np.atleast_1d(tempo)[0]); beats = list(map(float, bt))
    except ImportError:
        lags = np.arange(int(60 / 200 / dt), int(60 / 60 / dt))
        ac = np.array([np.dot(oenv[:-l], oenv[l:]) for l in lags])
        bpm = 60 / (lags[np.argmax(ac)] * dt); beats = []
    if pin: bpm = pin
    spb = 60 / bpm
    if pin or not beats:  # fit phase of a fixed grid to the onset envelope
        phases = np.linspace(0, spb, 64, endpoint=False)
        idx = lambda p: np.clip(np.round(np.arange(p, dur, spb) / dt).astype(int), 0, len(low) - 1)
        score = [low[idx(p)].sum() for p in phases]
        p0 = phases[int(np.argmax(score))] if phase is None else phase
        if p0 - spb > -0.06: p0 = max(0.0, p0 - spb)  # do not drop a beat that sits at t=0
        beats = list(np.arange(p0, dur - 0.05, spb))
    strength = [low[min(len(low) - 1, int(round(b / dt)))] for b in beats]
    k = 0 if phase is not None else int(np.argmax([sum(strength[i::4]) for i in range(4)]))
    if opt("--downbeat") is not None: k = int(opt("--downbeat"))
    downbeats = beats[k::4]
    thr = np.percentile(oenv, 92); hits, last = [], -1   # hits: onset peaks at least 90 ms apart
    for i in range(1, len(oenv) - 1):
        if oenv[i] > thr and oenv[i] >= oenv[i - 1] and oenv[i] >= oenv[i + 1] and i * dt - last > 0.09:
            hits.append(round(i * dt, 3)); last = i * dt
    out = {"bpm": round(bpm, 3), "duration": round(dur, 3), "beats": [round(b, 4) for b in beats],
           "downbeats": [round(b, 4) for b in downbeats], "hits": hits}
    json.dump(out, open(dst, "w"), indent=1)
    print(f"{dst}: {out['bpm']} BPM, {len(beats)} beats, {len(downbeats)} downbeats, {len(hits)} hits, first beat {beats[0]:.3f}s")

if __name__ == "__main__":
    main()
