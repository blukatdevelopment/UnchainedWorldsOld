#!/bin/bash
python3 bot.py &

export FLASK_APP=web/router.py
flask run --host=0.0.0.0