// lib/motion.js: stateless motion helpers. Every value is a pure function of t (seconds).
(function () {
  const clamp = (x, a = 0, b = 1) => (x < a ? a : x > b ? b : x);
  const lerp = (a, b, u) => a + (b - a) * u;
  const prog = (t, t0, d) => clamp((t - t0) / d);
  const E = {
    linear: x => x,
    outCubic: x => 1 - Math.pow(1 - x, 3),
    inCubic: x => x * x * x,
    inOutCubic: x => (x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2),
    outQuint: x => 1 - Math.pow(1 - x, 5),
    outExpo: x => (x >= 1 ? 1 : 1 - Math.pow(2, -10 * x)),
    inExpo: x => (x <= 0 ? 0 : Math.pow(2, 10 * x - 10)),
    inOutExpo: x => x <= 0 ? 0 : x >= 1 ? 1 : x < 0.5 ? Math.pow(2, 20 * x - 10) / 2 : (2 - Math.pow(2, -20 * x + 10)) / 2,
  };
  // Closed-form damped spring, 0 -> 1, t = seconds since trigger. No state between frames.
  const SPRING = { smooth: { k: 170, c: 26 }, snappy: { k: 320, c: 32 }, soft: { k: 90, c: 19 }, tiny: { k: 220, c: 24 } };
  function spring(t, cfg = SPRING.smooth) {
    if (t <= 0) return 0;
    const k = cfg.k, c = cfg.c, m = cfg.m || 1;
    const w0 = Math.sqrt(k / m), z = c / (2 * Math.sqrt(k * m));
    if (z < 1) {
      const wd = w0 * Math.sqrt(1 - z * z);
      return 1 - Math.exp(-z * w0 * t) * (Math.cos(wd * t) + (z * w0 / wd) * Math.sin(wd * t));
    }
    return 1 - Math.exp(-w0 * t) * (1 + w0 * t);
  }
  // A value with many targets = sum of one spring per change. keys: [[time, value], ...]
  function keyed(t, keys, cfg) {
    let v = keys[0][1];
    for (let i = 1; i < keys.length; i++) v += (keys[i][1] - keys[i - 1][1]) * spring(t - keys[i][0], cfg);
    return v;
  }
  const ramp = (t, t0, d, a, b, ease = E.inOutCubic) => lerp(a, b, ease(prog(t, t0, d)));
  // Seeded noise only. Never Math.random().
  function mulberry32(a) {
    return function () {
      a |= 0; a = (a + 0x6d2b79f5) | 0;
      let t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  // Beat grid from beats.json (injected as window.BEATS) or a fallback BPM. beat(4.5) = halfway through beat 4.
  function grid(B, bpm = 120) {
    const beats = (B && B.beats) || [];
    const spb = 60 / ((B && B.bpm) || bpm);
    const beat = i => {
      const f = Math.floor(i), fr = i - f;
      const at = n => (n < beats.length ? beats[n] : (beats.length ? beats[beats.length - 1] + (n - beats.length + 1) * spb : n * spb));
      return at(f) + fr * (at(f + 1) - at(f));
    };
    return { beat, spb, bpm: (B && B.bpm) || bpm };
  }
  // Sound cue registry. Register once at load, never inside seek().
  const cues = [];
  const cue = (t, type, gain = 1) => cues.push({ t: +t.toFixed(4), type, gain });
  window.M = { clamp, lerp, prog, E, SPRING, spring, keyed, ramp, mulberry32, grid, cue, cues };
})();
