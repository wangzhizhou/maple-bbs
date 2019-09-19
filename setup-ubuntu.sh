#!/usr/bin/env bash
#-*- coding:utf-8 -*-

sudo apt-get update

sudo apt-get install -y libjpeg-dev libpng-dev libfreetype6-dev 
sudo apt-get install -y python-virtualenv
sudo apt-get install -y python3
sudo apt-get install -y python3-dev
sudo apt-get install -y mysql-server
sudo apt-get install -y redis-server

virtualenv py3 -p python3

source ./py3/bin/activate
pip install -r requirements.txt
if [ ! -f config.py ]; 
then
	cp config.example config.py
fi

mkdir -p logs/

# config.py 

# config mysql
# su - 
# mysql
# create database bbs;
# create user joker@'%' identified by 'minecraft';
# grant all priviledges `bbs`.* to joker@'%';
# flush priviledges;

# config redis

sudo systemctl restart mysql.service
sudo systemctl restart redis-server.service

python runserver.py initdb
python runserver.py create-index
python runserver.py create-user
python runserver.py
