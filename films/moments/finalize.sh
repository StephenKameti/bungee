#!/bin/bash
# finalize.sh POSTER KEY [QUERY] [NAME]   run inside a film folder. Renders 16:9, 1:1, 9:16 at 60 fps with 4 subframes,
# builds SFX from cues.json, mixes to -14 LUFS (true peak headroom for AAC), muxes, and writes the poster.
set -e
POSTER=$1; KEY=$2; QUERY=${3:-}; NAME=${4:-final}
QA=""; [ -n "$QUERY" ] && QA="--q $QUERY"
node render.mjs --stills $POSTER $QA --stilldir review/poster_$NAME >/dev/null && cp review/poster_$NAME/000.png out/${NAME}_poster.png
DUR=$(node -p "require('./timeline.json').duration")
python3 sfx.py cues.json audio/sfx_$NAME.wav --dur $DUR --key $KEY >/dev/null
ffmpeg -v error -y -i audio/music.wav -i audio/sfx_$NAME.wav -filter_complex \
 "[0:a]volume=0.85[m];[1:a]volume=0.75[s];[m][s]amix=inputs=2:normalize=0:duration=first,atrim=0:$DUR,afade=t=out:st=$(awk "BEGIN{print $DUR-0.8}"):d=0.8,loudnorm=I=-14:TP=-2.2:LRA=11[a]" \
 -map "[a]" -ar 48000 audio/mix_$NAME.wav
for F in "1920 1080 16x9" "1080 1080 1x1" "1080 1920 9x16"; do
  set -- $F
  node render.mjs --w $1 --h $2 --fps 60 --sub 4 --poster $POSTER $QA --out out/silent_${NAME}_$3.mp4 >/dev/null
  ffmpeg -v error -y -i out/silent_${NAME}_$3.mp4 -i audio/mix_$NAME.wav -c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart out/${NAME}_$3.mp4
  rm -f out/silent_${NAME}_$3.mp4
  echo "done ${NAME}_$3 $(date +%T)"
done
