
#!/usr/bin/python3
import sys
sys.path.append('../')
from flask import Flask, request, make_response, url_for, redirect
from flask import render_template, jsonify
import os
from database import Db

app = Flask(__name__)
app.db = Db()

@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")

@app.route('/characters', methods=['GET'])
def character_sheets():
  return render_template("characters.html")

print("Webserver started.")