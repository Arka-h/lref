#!/bin/bash
TEMP_STORE=$PWD
. $2/venv/bin/activate
cd $2/HTML/frame
python jinja.py $1
deactivate
git add .
git commit --allow-empty-message -m \"$3\"
cd $TEMP_STORE
