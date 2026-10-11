#!/bin/bash
cd /home/claude/films/moments
while kill -0 5721 2>/dev/null; do sleep 20; done
./finalize.sh 3.6 D "" moments
echo "MOMENTS DONE $(date +%T)"
