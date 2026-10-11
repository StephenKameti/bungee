#!/bin/bash
# Third queue: deck 9:16 (reusing its finished mix), then cal, persona, strat.
cd /home/claude/films/skills
node render.mjs --w 1080 --h 1920 --fps 60 --sub 4 --poster 3.3 --q skill=deck --out out/silent_deck_9x16.mp4 >/dev/null
ffmpeg -v error -y -i out/silent_deck_9x16.mp4 -i audio/mix_deck.wav -c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart out/deck_9x16.mp4
rm -f out/silent_deck_9x16.mp4; echo "done deck_9x16 $(date +%T)"
for s in cal persona strat; do ./finalize.sh 3.3 A skill=$s $s; done
echo "QUEUE3 DONE $(date +%T)"
