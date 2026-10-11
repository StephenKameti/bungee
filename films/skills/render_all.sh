#!/bin/bash
# Waits for the suite render to finish, then renders the six skill films one after another (cues.json is shared, so never in parallel).
cd /home/claude/films/skills
while kill -0 1439 2>/dev/null; do sleep 20; done
for s in kv fsu deck cal persona strat; do ./finalize.sh 3.3 A skill=$s $s; done
echo "ALL SKILLS DONE $(date +%T)"
