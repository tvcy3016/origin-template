#!/home/tingyu/anaconda3/bin/python
# -*- coding: UTF-8 -*- 
from flask import Flask, render_template, request, send_from_directory, session, send_file, redirect, url_for
from lib import fnc, form
import time, os, html, cgi, base64

######################參數設定(S)######################
param = fnc.loadINI(os.getcwd())
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['UPLOAD_FOLDER'] = '%s/temp' % (os.getcwd())
#可以帶到html裡的變數
# app.jinja_env.globals['nowts'] = int(time.time())

######################參數設定(E)######################

######################首頁(S)######################
@app.route('/')
def index():
    ####導去登入頁，也許未來做個煞有其事的首頁
    return redirect(url_for('login'))
######################首頁(E)######################

######################登入模組(S)######################
@app.route('/login', methods=['GET', 'POST'])
def login():
    ####
    uform = form.UserForm()
    try:
        if uform.validate_on_submit():
            return redirect(url_for('private'))
        else:
            return render_template('login.html', form = uform)
    except: 
        return render_template('login.html', form = uform)
    
#先經過這邊，不然每次上一頁都會有要不要再送出的錯誤訊息
@app.route('/private', methods=['GET', 'POST'])
def private():
    if request.method == 'POST':
        ####驗證
        if fnc.valid_login(request.form['passwd']):
            return redirect(url_for('login'))
        else:
            return redirect(url_for('login'))
######################登入模組(E)######################

######################登出模組(S)######################
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return '%s<br><a href = "/">%s</a>' % ("登出成功", "回到登入頁")
######################登出模組(E)######################


if __name__ == '__main__': 
    app.run(ssl_context=(param['pempath'], param['keypath']),host=param['host'],port=param['port'])