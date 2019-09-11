#!/usr/bin/env bash

sudo apt-get install -y libjpeg8-dev python-virtualenv python3 python3-dev
virtualenv py3 -p python3
source ./py3/bin/activate
pip install -r requirements.txt
cp config.example config.py
mkdir logs
python runserver.py initdb
python runserver.py create_index
python runserver.py create_user
