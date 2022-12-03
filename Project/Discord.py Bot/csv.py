import csv
from pymongo import MongoClient

mongoClient = MongoClient() 
db = mongoClient.october_mug_talk
db.segment.drop()

header = [ "name", "age", "country"]
csvfile = open('employee.csv', 'r')
reader = csv.DictReader( csvfile )

for each in reader:
    row={}
    for field in header:
        row[field]=each[field]
        
    print (row)
    db.segment.insert(row)