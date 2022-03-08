#!/bin/bash
#Stopping exixting Flask Server
echo "Install flask"
apt update -y
apt install python3-pip -y

# Create our directory
DIR="/home/ec2-user/flask-app"
if [ -d "$DIR" ]; then 
  echo "${DIR} exist"
else
  echo "Creating ${DIR} directory"
  mkdir ${DIR}
fi
