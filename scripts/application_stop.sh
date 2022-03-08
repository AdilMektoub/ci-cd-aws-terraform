#!/bin/bash
#Stopping exixting Flask Server
echo "Stopping any existing flask server"
lsof -nti:5000 | xargs kill -9