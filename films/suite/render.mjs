// render.mjs: deterministic frame renderer. Seeks index.html to each time, captures, pipes to ffmpeg.
// node render.mjs [--w 1920 --h 1080] [--fps 60] [--sub 4] [--shutter 0.5] [--from 0 --to 20]
//                 [--beats beats.json] [--poster 9.5] [--out out/silent.mp4]
//                 [--stills 0.5,2,4.25] [--contact 1]   (contact: one still per N beats -> review/contact.png)
//                 [--format png|jpeg]   Animatic: --w 960 --h 540 --fps 30 --sub 1 --format jpeg
import { chromium } from "playwright";
import { spawn, spawnSync } from "node:child_process";
import fs from "node:fs";
import path from "node:path";

const arg = (k, d) => { const i = process.argv.indexOf("--" + k); return i > 0 ? process.argv[i + 1] : d; };
const W = +arg("w", 1920), H = +arg("h", 1080), FPS = +arg("fps", 60), SUB = +arg("sub", 4), SHUT = +arg("shutter", 0.5);
const OUT = arg("out", "out/silent.mp4"), BEATS = arg("beats", "beats.json"), POSTER = arg("poster", null);
const page_url = "file://" + path.resolve(arg("page", "index.html")) + `?w=${W}&h=${H}` + (arg("q") ? "&" + arg("q") : "");

const browser = await chromium.launch({ executablePath: process.env.CHROME_PATH || undefined });
const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
const beats = fs.existsSync(BEATS) ? JSON.parse(fs.readFileSync(BEATS, "utf8")) : null;
await page.addInitScript(b => { window.BEATS = b; }, beats);
page.on("pageerror", e => { console.error("PAGE ERROR:", e.message); process.exit(1); });
await page.goto(page_url);
await page.evaluate(() => window.ready);                       // fonts + images decoded before frame 0
const DUR = +arg("to", await page.evaluate(() => window.DURATION));
const FROM = +arg("from", 0);
fs.mkdirSync("out", { recursive: true }); fs.mkdirSync("review", { recursive: true });
fs.writeFileSync("cues.json", JSON.stringify(await page.evaluate(() => window.M.cues), null, 1));
fs.writeFileSync("timeline.json", JSON.stringify({ duration: await page.evaluate(() => window.DURATION), bpm: beats?.bpm ?? 120 }));

// Raw CDP capture is ~4x faster than page.screenshot (which waits for stability checks). PNG = lossless.
const cdp = await page.context().newCDPSession(page);
const FMT = arg("format", "png");
const shot = async t => {
  await page.evaluate(x => window.seek(x), t);
  const { data } = await cdp.send("Page.captureScreenshot", { format: FMT, quality: FMT === "jpeg" ? 92 : undefined, optimizeForSpeed: true });
  return Buffer.from(data, "base64");
};

if (arg("stills") || arg("contact")) {
  const dir = arg("stilldir", "review/stills"); fs.rmSync(dir, { recursive: true, force: true }); fs.mkdirSync(dir, { recursive: true });
  let times = arg("stills") ? arg("stills").split(",").map(Number) : [];
  if (arg("contact")) { const n = +arg("contact"); const b = beats ? beats.beats : [...Array(Math.ceil(DUR * 2)).keys()].map(i => i / 2); times = b.filter((_, i) => i % n === 0).map(x => x + 0.25 * (60 / (beats?.bpm || 120))).filter(x => x < DUR); }
  for (const [i, t] of times.entries()) fs.writeFileSync(`${dir}/${String(i).padStart(3, "0")}.png`, await shot(t));
  const cols = Math.min(+arg("cols", 8), times.length), rows = Math.ceil(times.length / cols);
  const sheet = arg("sheet", "review/contact.png");
  spawnSync("ffmpeg", ["-v", "error", "-y", "-i", `${dir}/%03d.png`, "-vf", `scale=${arg("tw", 480)}:-1,tile=${cols}x${rows}:padding=6:color=black`, "-frames:v", "1", sheet]);
  console.log(`stills: ${times.length} -> ${dir}/ and ${sheet}`);
  await browser.close(); process.exit(0);
}

// Motion blur: SUB subframes per output frame across the shutter, averaged by ffmpeg tmix, then decimated.
const ff = spawn("ffmpeg", ["-v", "error", "-y", "-f", "image2pipe", "-framerate", String(FPS * SUB), "-i", "-",
  "-vf", SUB > 1 ? `tmix=frames=${SUB},select='eq(mod(n\\,${SUB})\\,${SUB - 1})',setpts=N/(${FPS}*TB)` : "null",
  "-r", String(FPS), "-c:v", "libx264", "-preset", "medium", "-crf", "16", "-pix_fmt", "yuv420p", "-movflags", "+faststart", OUT],
  { stdio: ["pipe", "inherit", "inherit"] });
const total = Math.round((DUR - FROM) * FPS), t0 = Date.now();
for (let f = 0; f < total; f++) {
  for (let s = 0; s < SUB; s++) {
    let t = FROM + (f + (SUB > 1 ? SHUT * s / SUB : 0)) / FPS;
    if (f === 0 && POSTER != null && FROM === 0) t = +POSTER;   // bake the poster as frame 0: same length, same sync
    const buf = await shot(t);
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once("drain", r));
  }
  if (f % FPS === 0) process.stdout.write(`\rframe ${f}/${total}  ${((Date.now() - t0) / 1000).toFixed(0)}s`);
}
ff.stdin.end(); await new Promise(r => ff.on("close", r)); await browser.close();
console.log(`\n${OUT}: ${total} frames at ${FPS} fps, ${SUB} subframes, ${W}x${H}`);
