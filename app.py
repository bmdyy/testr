#!/usr/bin/python3 
from flask import Flask, render_template, request
import sqlite3
import setup_db
import subprocess

app = Flask(__name__)
con = sqlite3.connect('testr.db')

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/editor', methods=['GET','POST'])
def editor():
    if request.method == 'GET':
        return render_template('editor.html', code='', out='')

    elif request.method == 'POST':
        code = request.form['code']
        try:
            output = subprocess.check_output(['python3','-c',code], stderr=subprocess.STDOUT)
            output = output.decode('utf-8')
        except subprocess.CalledProcessError as exc:
            return render_template('editor.html', code=code, out="%s"%exc.output.decode('utf-8'))
        else:
            return render_template('editor.html', code=code, out=output)

if __name__ == '__main__':
    setup_db.seed_db()
    app.run(host='0.0.0.0',port='5000')