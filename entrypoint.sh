#!/bin/bash

python3 configure_app.py

uvicorn app.app:app --host 0.0.0.0 --port 8080 --workers 4 --log-level critical