# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pymongo
import xlrd
import os

client     = pymongo.MongoClient("mongodb://localhost:27017/")
db         = client['KBC']
QCol       = db['Questions']

Book  = xlrd.open_workbook('Data.xlsx')
Sheet = Book.sheet_by_index(0)

dict_1 = {}
for row in range (Sheet.nrows):
    Heading = str(Sheet.cell(row,0)).replace('text:','')[1:-1]
    Description = str(Sheet.cell(row,1)).replace('text:','')[1:-1]
    Image = str(Sheet.cell(row,2)).replace('text:','')[1:-1]
    RowData     = {'Heading':Heading,'Description':Description, 'Image':Image}
    x = QCol.insert_one(RowData)

for z in QCol.find():
  print(z)
  

