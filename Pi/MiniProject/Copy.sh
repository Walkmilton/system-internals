#!/bin/sh

#  Copy.sh
#  
#
#  Created by Declan Doyle on 13/12/2019.
#  

sudo scp -i piNMAP.pem ubuntu@52.56.169.42:/home/ubuntu/command.sh .
sudo -E ./Script.sh
