#!/bin/bash
# Re-render kv after the queue (ratio label timing fix). Waits for the Moments render to finish.
cd /home/claude/films/skills
while pgrep -f "render_after.sh" >/dev/null; do sleep 20; done
./finalize.sh 3.3 A skill=kv kv
echo "KV RERENDER DONE $(date +%T)"
