// lib/kit.js: Bungee film kit. Stage, placement, the cord, the logo lockup and shared motion helpers.
// Every function is a pure function of t. Requires lib/motion.js first.
(function () {
  const { clamp, lerp, prog, E, SPRING, spring, keyed } = M;
  const q = new URLSearchParams(location.search);
  const W = +q.get("w") || 1920, H = +q.get("h") || 1080;
  const S = Math.min(W, H) / 1080;
  const wide = W / H > 1.2, portrait = H / W > 1.2;
  const BUNGEE = { k: 200, c: 14 };            // brand moments only: one visible overshoot
  const C = { slate: "#3F414B", lime: "#BEFD50", paper: "#F6F6F2", hair: "#DCDDD6", muted: "#5E6069", white: "#FFFFFF",
              sand: "#D9D5C7", steel: "#8C93A8", red: "#C8463D", board: "#ECECE5" };
  const stage = document.getElementById("stage");
  stage.style.width = W + "px"; stage.style.height = H + "px";
  const $ = id => document.getElementById(id);

  // First time a spring crosses 1 (the landing frame), so drops can be timed to land on a beat.
  function landTime(cfg) { for (let t = 0.001; t < 2; t += 0.001) if (spring(t, cfg) >= 1) return t; return 0.3; }

  // place: x, y in design px from stage centre. anchor: c (centre), l (left edge), t (top centre)
  function place(el, x, y, s = 1, o = 1, opt = {}) {
    const a = opt.anchor || "c";
    const tx = a === "l" ? "0%" : "-50%", ty = a === "t" ? "0%" : "-50%";
    const sx = opt.sx != null ? opt.sx : 1, sy = opt.sy != null ? opt.sy : 1;
    el.style.transformOrigin = a === "l" ? "0 50%" : a === "t" ? "50% 0" : "50% 50%";   // scale about the anchor so low-res previews match
    el.style.transform = `translate(${tx},${ty}) translate(${x * S}px,${y * S}px) rotate(${opt.rot || 0}deg) scale(${s * S * sx},${s * S * sy})`;
    el.style.opacity = o;
    el.style.visibility = o <= 0.002 ? "hidden" : "visible";
    if (opt.blur != null) el.style.filter = opt.blur > 0.05 ? `blur(${opt.blur}px)` : "none";
  }
  const life = (t, tin, tout, din = 0.3, dout = 0.22) => Math.min(E.outCubic(prog(t, tin, din)), 1 - E.inCubic(prog(t, tout, dout)));
  // Slam: fast in with scale and blur settling. Returns values for place().
  function slam(t, t0, cfg = SPRING.snappy) {
    const p = spring(t - t0, cfg);
    return { p, s: lerp(1.12, 1, clamp(p)), blur: (1 - clamp(p)) * 10, o: clamp(p * 1.6), dy: (1 - clamp(p)) * 34 };
  }
  // Colour keyed by springs: keys [[t, "#rrggbb"], ...]
  const hex = h => [1, 3, 5].map(i => parseInt(h.slice(i, i + 2), 16));
  function keyedColor(t, keys, cfg = SPRING.smooth) {
    const ch = [0, 1, 2].map(i => keyed(t, keys.map(k => [k[0], hex(k[1])[i]]), cfg));
    return `rgb(${ch.map(v => Math.round(clamp(v, 0, 255))).join(",")})`;
  }
  // The cord: a lime line hanging from above the frame to (x, yEnd).
  function cord(el, x, yEnd, o = 1) {
    const top = -H / 2 / S - 300;
    const h = Math.max(0, yEnd - top);
    el.style.height = h * S + "px";
    el.style.transform = `translate(-50%,0) translate(${x * S}px,${(top) * S}px)`;
    el.style.opacity = o; el.style.visibility = o <= 0.002 || h < 1 ? "hidden" : "visible";
  }
  // Fit a text element's font size so its width stays within maxW (design px). Call after fonts load.
  function fit(el, base, maxW) {
    el.style.fontSize = base + "px";
    const w = el.offsetWidth;
    if (w > maxW) el.style.fontSize = Math.floor(base * maxW / w) + "px";
    return parseFloat(el.style.fontSize);
  }
  window.K = { W, H, S, wide, portrait, BUNGEE, C, $, landTime, place, life, slam, keyedColor, cord, fit };
})();
