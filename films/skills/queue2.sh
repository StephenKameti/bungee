#!/bin/bash
# Second queue: waits for the Moments render, then finishes fsu (1:1, 9:16) and renders kv, deck, cal, persona, strat.
cd /home/claude/films/skills
while pgrep -f "render_after.sh" >/dev/null; do sleep 20; done
for F in "1080 1080 1x1" "1080 1920 9x16"; do set -- $F
  node render.mjs --w $1 --h $2 --fps 60 --sub 4 --poster 3.3 --q skill=fsu --out out/silent_fsu_$3.mp4 >/dev/null
  ffmpeg -v error -y -i out/silent_fsu_$3.mp4 -i audio/mix_fsu.wav -c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart out/fsu_$3.mp4
  rm -f out/silent_fsu_$3.mp4; echo "done fsu_$3 $(date +%T)"
done
for s in kv deck cal persona strat; do ./finalize.sh 3.3 A skill=$s $s; done
echo "QUEUE2 DONE $(date +%T)"
