#!/bin/sh
export FLASK_APP=src/resources.py
source venv/bin/activate
flask run -h 0.0.0.0