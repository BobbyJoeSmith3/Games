#==================================================================
#filename: views.py
#this script holds a series of functions that tells flask where it 
#can find the html code on the server to render on the browswer
#==================================================================
#Make the site capable of utilizing characters from multiple langauges
# -*- coding: utf-8 -*-

from app import app
from flask import render_template

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/activate_venv')
def activate_venv():
	return render_template('activate_venv.html')

@app.route('/create_venv')
def create_venv():
	return render_template('create_venv.html')

@app.route('/install_flask')
def install_flask():
	return render_template('install_flask.html')

@app.route('/launch_flask_locally')
def launch_flask_locally():
	return render_template('launch_flask_locally.html')

@app.route('/view_flask_app')
def view_flask_app():
	return render_template('view_flask_app.html')

@app.route('/hello_world')
def hello_world():
	return render_template('hello_world.html')

@app.route('/render_html')
def render_html():
	return render_template('render_html.html')

@app.route('/html_links')
def html_links():
	return render_template('html_links.html')

