"""sfx.py: synthesize UI sound effects from cues.json into one stem, tuned to the score's key.
Cue types: click, tick, type, pop, whoosh, thump, chime.
Usage: python3 sfx.py cues.json audio/sfx.wav --dur 12.0 --key A
"""
import json, sys, wave
import numpy as np

SR = 48000
NOTE = {"C": 0, "C#": 1, "D": 2, "D#": 3, "E": 4, "F": 5, "F#": 6, "G": 7, "G#": 8, "A": 9, "A#": 10, "B": 11}
rng = np.random.default_rng(11)

def tt(s): return np.arange(int(s * SR)) / SR
def hz(m): return 440 * 2 ** ((m - 69) / 12)

def click():
    t = tt(0.03); x = rng.uniform(-1, 1, len(t)) * np.exp(-t * 900) * 0.5
    return x + 0.35 * np.sin(2 * np.pi * 3200 * t) * np.exp(-t * 400)

def tick():
    t = tt(0.02); return 0.3 * np.sin(2 * np.pi * 2400 * t) * np.exp(-t * 500)

def pop(f):
    t = tt(0.12); ff = f * (1 + 0.6 * np.exp(-t * 60))
    return 0.45 * np.sin(2 * np.pi * np.cumsum(ff) / SR) * np.exp(-t * 35)

def whoosh(d=0.32):
    t = tt(d); n = rng.uniform(-1, 1, len(t)); out = np.zeros_like(n); lp = 0.0
    a = 0.02 + 0.25 * np.sin(np.pi * t / d) ** 2  # sweeping one pole low pass
    for i in range(len(n)): lp += a[i] * (n[i] - lp); out[i] = lp
    return out * np.sin(np.pi * t / d) ** 1.5 * 1.1

def thump(f):
    t = tt(0.45); ff = f * 0.5 * (1 + 1.2 * np.exp(-t * 40))
    body = np.sin(2 * np.pi * np.cumsum(ff) / SR) * np.exp(-t * 7)
    return 0.8 * np.tanh(1.6 * body) + 0.15 * rng.uniform(-1, 1, len(t)) * np.exp(-t * 80)

def chime(f):
    t = tt(1.2); return 0.22 * sum(np.sin(2 * np.pi * f * k * t) * np.exp(-t * (3 + 2 * k)) / k for k in (1, 2, 3, 4.2))

def main():
    cues = json.load(open(sys.argv[1])); out_path = sys.argv[2]
    dur = float(sys.argv[sys.argv.index("--dur") + 1]); key = sys.argv[sys.argv.index("--key") + 1] if "--key" in sys.argv else "A"
    root = 57 + NOTE[key]; penta = [0, 3, 5, 7, 10]  # minor pentatonic of the score's key
    buf = np.zeros(int((dur + 1.5) * SR)); pi = 0
    for c in sorted(cues, key=lambda c: c["t"]):
        k = c["type"]; g = c.get("gain", 1)
        if k == "click": x = click()
        elif k == "tick": x = tick()
        elif k == "type": x = tick() * rng.uniform(0.6, 1.0)
        elif k == "pop": x = pop(hz(root + 12 + penta[pi % 5])); pi += 1
        elif k == "whoosh": x = whoosh(c.get("len", 0.32)); c["t"] -= 0.12  # whoosh peaks into the motion
        elif k == "thump": x = thump(hz(root - 12))
        elif k == "chime": x = chime(hz(root + 12))
        else: continue
        i = max(0, int(c["t"] * SR)); j = min(len(buf), i + len(x)); buf[i:j] += g * x[: j - i]
    buf = buf[: int(dur * SR)]
    buf /= max(1.0, np.max(np.abs(buf)) / 0.7)
    st = np.stack([buf, buf], 1)
    with wave.open(out_path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st * 32767).astype(np.int16).tobytes())
    print(f"{out_path}: {len(cues)} cues")

if __name__ == "__main__":
    main()
