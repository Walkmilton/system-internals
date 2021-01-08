#!/bin/sh

sudo insmod piio.ko
sudo ./piio writepin 23 1
/usr/bin/python3 /home/pi/MiniProject/MQTT\ Subscribe.py
