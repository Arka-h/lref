#!/bin/bash
TEMP_STORE=$PWD
activate
python jinja.py $1
cd $2/HTML
git add .
git commit --allow-empty-message -m \"$3\"
cd $TEMP_STORE
deactivate
