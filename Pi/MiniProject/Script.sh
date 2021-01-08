#!/bin/sh

#  Script.sh
#  
#
#  Created by Declan Doyle on 11/12/2019.
#  

chmod +x command.sh
./piio writepin 23 0
cd /home/pi/MiniProject
./command.sh &
pid=$!

while kill -0 $pid 2> /dev/null; do
    ./piio toggle 25 5 1
    sleep 0.75
done

xsltproc output.xml -o output.html

sudo scp -i piNMAP.pem output.html ubuntu@52.56.169.42:/home/ubuntu/
sudo ssh -i piNMAP.pem ubuntu@52.56.169.42 sudo ./copy.sh


./piio writepin 8 1
sleep 5
./piio writepin 8 0
./piio writepin 23 1

pkill python3
/usr/bin/python3 /home/pi/MiniProject/MQTT\ Subscribe.py
