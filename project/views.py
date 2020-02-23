from . import app
from flask import render_template, request
import pymongo
from bson import ObjectId
import os
os.environ["PYTHONIOENCODING"] = "utf-8"

@app.route('/')
def index():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db  = client['KBC']
    col = db['Questions']
    Heading = []
    Description = []
    Image = []
    Ids = []
    for each in col.find({}):
        Ids.append(each['_id'])
        Heading.append(each['Heading'])
        Description.append(each['Description'])
        Image.append(each['Image'])
    return render_template('index.html', len = len(Ids), Ids=Ids, Heading=Heading, Description=Description, Image=Image)

@app.route('/details/<string:Id>')
def details(Id):
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db  = client['KBC']
    col = db['Questions']
    Heading = []
    Description = []
    Image = []
    for each in col.find({'_id': ObjectId(Id) }):
        Heading = each['Heading']
        Description = each['Description']
        Image = each['Image']
    print(Heading)
    return render_template('details.html', Heading=Heading, Description=Description, Image=Image)