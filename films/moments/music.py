"""music.py: synthesize an original score in code. numpy only.
Usage: python3 music.py --bpm 120 --bars 6 --style clean --key A --out audio/music.wav
Styles: clean (minimal four on the floor), amapiano (log drum bass, shakers), cinematic (sparse pulse)
"""
import argparse, wave
import numpy as np

SR = 48000
NOTE = {"C": 0, "C#": 1, "D": 2, "D#": 3, "E": 4, "F": 5, "F#": 6, "G": 7, "G#": 8, "A": 9, "A#": 10, "B": 11}

def hz(midi): return 440.0 * 2 ** ((midi - 69) / 12)

def env(n, a=0.002, d=0.2):
    t = np.arange(n) / SR
    return np.minimum(1, t / max(a, 1e-4)) * np.exp(-t / d)

def place(buf, x, start, gain=1.0):
    i = int(start * SR)
    if i >= len(buf): return
    j = min(len(buf), i + len(x))
    buf[i:j] += gain * x[: j - i]

def kick(len_s=0.35):
    n = int(len_s * SR); t = np.arange(n) / SR
    f = 45 + 110 * np.exp(-t * 35)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 9) * 0.9

def noise(n, rng): return rng.uniform(-1, 1, n)

def hat(rng, len_s=0.05):
    n = int(len_s * SR); x = np.diff(noise(n + 1, rng)); return x * env(n, 0.001, 0.012) * 0.25

def clap(rng):
    n = int(0.18 * SR); x = noise(n, rng)
    x = np.convolve(x, np.ones(6) / 6, "same") - np.convolve(x, np.ones(40) / 40, "same")
    e = env(n, 0.001, 0.05) + 0.6 * np.roll(env(n, 0.001, 0.02), int(0.012 * SR))
    return x * e * 0.5

def pluck(freq, len_s=0.6, bright=0.5):
    n = int(len_s * SR); t = np.arange(n) / SR
    x = sum((bright ** (h - 1)) * np.sin(2 * np.pi * freq * h * t) / h for h in range(1, 6))
    return x * env(n, 0.003, 0.18) * 0.22

def bass(freq, len_s, style):
    n = int(len_s * SR); t = np.arange(n) / SR
    if style == "amapiano":  # log drum: pitched, gliding, saturated
        f = freq * (1 + 0.5 * np.exp(-t * 30))
        x = np.tanh(2.2 * np.sin(2 * np.pi * np.cumsum(f) / SR)) * np.exp(-t * 4.5)
        return x * 0.45
    x = np.sin(2 * np.pi * freq * t) + 0.3 * np.sin(2 * np.pi * 2 * freq * t)
    return x * env(n, 0.005, 0.25) * 0.35

def reverb(x, rng, seconds=0.9, mix=0.14):
    n = int(seconds * SR); ir = noise(n, rng) * np.exp(-np.arange(n) / SR * 5.5)
    ir /= np.sqrt(np.sum(ir ** 2))
    wet = np.fft.irfft(np.fft.rfft(x, len(x) + n) * np.fft.rfft(ir, len(x) + n))[: len(x)]
    return x + mix * wet

def write_wav(path, x):
    x = np.clip(x, -1, 1); st = np.stack([x, x], 1)
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((st * 32767).astype(np.int16).tobytes())

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bpm", type=float, default=120); ap.add_argument("--bars", type=int, default=8)
    ap.add_argument("--style", default="clean", choices=["clean", "amapiano", "cinematic"])
    ap.add_argument("--key", default="A"); ap.add_argument("--tail", type=float, default=1.5)
    ap.add_argument("--seed", type=int, default=7); ap.add_argument("--out", default="audio/music.wav")
    a = ap.parse_args()
    rng = np.random.default_rng(a.seed)
    spb = 60 / a.bpm; beats = a.bars * 4
    buf = np.zeros(int((beats * spb + a.tail) * SR))
    root = 45 + NOTE[a.key]  # A2 = 45
    prog = [0, -4, 3, -2]  # minor: i  VI  III  VII
    chord = lambda r: [r, r + 3, r + 7, r + 12]
    swing = 0.06 * spb if a.style == "amapiano" else 0
    for b in range(beats):
        t = b * spb; bar = b // 4; r = root + prog[bar % 4]; last = bar == a.bars - 1
        if a.style != "cinematic" or b % 4 == 0:
            if not (last and b % 4 == 3): place(buf, kick(), t, 1.0 if b % 4 == 0 else 0.85)
        if a.style != "cinematic":
            place(buf, hat(rng), t + spb / 2 + swing, 0.9)
            if b % 4 in (1, 3) and not last: place(buf, clap(rng), t, 0.8)
        if a.style == "amapiano":
            for s in range(4): place(buf, hat(rng, 0.03), t + s * spb / 4 + (swing if s % 2 else 0), 0.35 + 0.25 * (s % 2))
            if b % 2 == 0 or b % 4 == 3: place(buf, bass(hz(r), spb * 1.4, "amapiano"), t + (spb / 2 if b % 4 == 3 else 0))
        elif b % 4 == 0:
            place(buf, bass(hz(r), spb * 4, a.style), t)
        if b % 2 == 1 or a.style == "cinematic":
            for k, m in enumerate(chord(r + 12)): place(buf, pluck(hz(m), 0.5 if not last else 2.2), t + spb / 2 + k * 0.012, 0.8)
    end = beats * spb  # final resolve on the downbeat after the grid
    place(buf, kick(), end, 0.9)
    for k, m in enumerate(chord(root + 12)): place(buf, pluck(hz(m), 2.0, 0.35), end + k * 0.015, 1.0)
    out = reverb(buf, rng)
    fade = int(0.4 * SR); out[-fade:] *= np.linspace(1, 0, fade)
    out = np.tanh(out * 1.2); out /= np.max(np.abs(out)) / 0.89  # peak about -1 dBFS
    write_wav(a.out, out)
    print(f"{a.out}: {len(out)/SR:.2f}s at {a.bpm} BPM, {a.bars} bars, style {a.style}")

if __name__ == "__main__":
    main()
