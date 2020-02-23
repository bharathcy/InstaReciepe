from . import app
from flask import render_template
import pymongo
import xlrd
import os
os.environ["PYTHONIOENCODING"] = "utf-8"

f1 = open(os.getcwd()+'\\book.txt','r', encoding="utf8").readlines()#, encoding(utf8)

@app.route('/')
def index():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db  = client['KBC']
    col = db['Questions']
    Data = {}
    for each in col.find():
        print(each)
        Data.update(each)

    return render_template('index.html',string=f1)