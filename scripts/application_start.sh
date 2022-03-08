#!/bin/bash

# give permission
sudo chmod -R 777 /home/ec2-user/flask-app

# on directory
cd /home/ec2-user/flask-app

# Install dependancies
pip3 install -r requirements.txt

# add to the path
export FLASK_APP=app.py

# launch app
python3 app.py