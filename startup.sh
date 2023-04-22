#!/usr/bin/env bash
# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn main:app \
    --bind 0.0.0.0:$PORT \
    --workers 4 \
    --timeout 300