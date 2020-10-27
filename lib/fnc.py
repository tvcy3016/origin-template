# coding=UTF-8
import sqlite3, configparser, sys, os, base64,json,html
import pandas as pd
import time, datetime

######讀取設定檔
def loadINI(s_path,ini='setting'):
    cfgpath = '%s/%s.ini' % (s_path,ini)
    # 創建對象
    conf = configparser.ConfigParser()
    # 讀取INI
    conf.read(cfgpath, encoding='utf-8')
    # 取得所有sections
    sections = conf.sections()
    # 取得某section之所有items，返回格式為list
    param = {}
    for sS in sections:
        items = conf.items(sS)
        for item in items:
            param[item[0]] = item[1]
    return param

######連線資料庫
def connect_db(ini='setting'):
    param = loadINI(os.getcwd(),ini)
    conn=sqlite3.connect(param['dbpath'])
    db = conn.cursor()
    return conn, db


######檢索指令
#S=查詢
#I=新增
#U=修改
#D=刪除
def query(query,status="S",ini='setting'):
    conn, db = connect_db(ini)
    db.execute("%s" % (query))
    if status == 'S':
        rows = db.fetchall()
    else:
        rows = ''
    conn.commit()
    conn.close()
    return rows

######驗證登入
def valid_login(password): 
    check = 0
    try: check = 1

    except: pass
    return check
    
######確認session身分
def valid_session(password,ini='setting'): 
    param = loadINI(os.getcwd(),ini)
    check = 0
    try: check = 1
        
    except: pass
    return check
