#=========================================
#filename: run.py
#This script launches a flask app
#=========================================
#Make the site able to support characters from other languages
# -*- coding: utf-8 -*-
#!venv/bin/python

from app import app
app.run(debug=True)