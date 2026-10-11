#!/bin/bash
# sheet.sh SKILL FMT  -> review/contact_SKILL_FMT.png (one still per beat pair)
SK=$1; F=${2:-16x9}
case $F in 16x9) WH="--w 1920 --h 1080"; TW=360;; 1x1) WH="--w 1080 --h 1080"; TW=240;; 9x16) WH="--w 1080 --h 1920"; TW=200;; esac
node render.mjs $WH --q skill=$SK --contact 2 --tw $TW --cols 8 --sheet review/contact_${SK}_$F.png --stilldir review/st_${SK}_$F 2>&1 | grep -v "^stills"; true
