#===========================================================
#filename: __init__.py
#This script tells the computer to execute this script first
#when sourcing the app folder
#===========================================================
#Make the site capable of utilizing characters from multiple langauges
# -*- coding: utf-8 -*-

from flask import Flask 

app = Flask(__name__)
app.config.from_object('config')

from app import views