#!/bin/bash
# package.sh: QA every final, copy films and posters to outputs, build contact sheets and the source zip.
set -e
OUT=/mnt/user-data/outputs/films; mkdir -p $OUT/contact
SP=/tmp/claude-0/-home-claude/765eb2c9-2803-5faf-8405-c4e6db1e1ea8/scratchpad
echo "| file | size | fps | frames | length | loudness | true peak | frame 0 vs poster |" > QA.md
echo "|---|---|---|---|---|---|---|---|" >> QA.md
for d in suite moments skills; do
  for f in $d/out/*_16x9.mp4 $d/out/*_1x1.mp4 $d/out/*_9x16.mp4; do
    [ -f "$f" ] || continue; n=$(basename $f .mp4); id=${n%_*}
    case $n in silent*|anim*) continue;; esac
    wh=$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height,r_frame_rate,nb_frames -of csv=p=0 $f)
    dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $f)
    lu=$(ffmpeg -hide_banner -i $f -af ebur128=peak=true -f null - 2>&1 | grep -E "^\s+I:" | awk '{print $2}')
    pk=$(ffmpeg -hide_banner -i $f -af ebur128=peak=true -f null - 2>&1 | grep -E "^\s+Peak:" | awk '{print $2}')
    ffmpeg -v error -y -i $f -frames:v 1 $SP/f0.png
    if [[ $n == *16x9 ]]; then ps=$(ffmpeg -hide_banner -i $SP/f0.png -i $d/out/${id}_poster.png -lavfi psnr -f null - 2>&1 | grep -o "average:[0-9.]*" | cut -d: -f2); else ps="n/a"; fi
    IFS=, read w h r nf <<< "$wh"
    echo "| $n.mp4 | ${w}x${h} | $r | $nf | ${dur}s | $lu LUFS | $pk dBFS | ${ps} dB |" >> QA.md
    cp $f $OUT/
  done
  for p in $d/out/*_poster.png; do [ -f "$p" ] && cp $p $OUT/; done
done
# Contact sheets from the finals: one frame per second, 16:9 and 9:16
for f in $OUT/*_16x9.mp4 $OUT/*_9x16.mp4; do n=$(basename $f .mp4)
  D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $f | cut -d. -f1)
  case $n in *16x9) S="scale=384:-1"; R=3;; *) S="scale=216:-1"; R=2;; esac
  C=$(( (D + R - 1) / R ))
  ffmpeg -v error -y -i $f -vf "fps=1,$S,tile=${C}x${R}:padding=6:color=0x1a1a1a" -frames:v 1 $OUT/contact/${n}_contact.png
done
cp README.md CAPTIONS.md QA.md $OUT/
# Source zip (no node_modules, renders or scratch stills)
cd /home/claude && rm -f $OUT/bungee-films-source.zip
zip -qr $OUT/bungee-films-source.zip films -x "films/*/node_modules/*" "films/node_modules/*" "films/*/out/*" "films/*/review/st_*" "films/*/review/tr*" "films/*/review/fin_*" "films/*/review/tmp*" "films/*/review/chk*" "films/*/review/det_*" "films/*/review/poster_*" "films/*/audio/sfx_*" "films/*/audio/mix_*" "films/*/review/*.png" "films/*/review/*.log"
ls -la $OUT $OUT/contact | head -60
