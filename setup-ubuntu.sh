#!/usr/bin/env bash
#-*- coding:utf-8 -*-

sudo apt-get update

sudo apt-get install -y libjpeg-dev
sudo apt-get install -y python-virtualenv
sudo apt-get install -y python3
sudo apt-get install -y python3-dev
sudo apt-get install -y mysql-server

virtualenv py3 -p python3

source ./py3/bin/activate
pip install -r requirements.txt
if [ ! -f config.py ]; 
then
	cp config.example config.py
fi

#python runserver.py initdb
#python runserver.py create_index
#python runserver.py create_user
