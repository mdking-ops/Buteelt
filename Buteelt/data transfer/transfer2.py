import pandas as pd
import pyodbc
from pymongo import MongoClient

server = 'DESKTOP-M86GRUG/SQLEXPRESS'
database = 'ULAANBAATAR'
mongo_uri = 'mongodb://localhost:27017/'
mongo_db = 'company' 
mongo_collection = 'employee'  

conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')

query = "SELECT * FROM EMPLOYEES WHERE ХЭЛТЭС LIKE '%IT%'"
cursor = conn.cursor()
cursor.execute(query)

rows = cursor.fetchall()
columns = [column[0] for column in cursor.description]
df = pd.DataFrame.from_records(rows, columns=columns)

conn.close()

client = MongoClient(mongo_uri)
db = client[mongo_db]
collection = db[mongo_collection]

data = df.to_dict(orient='records')

collection.insert_many(data)

client.close()
