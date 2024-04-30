import pandas as pd
import pyodbc
from pymongo import MongoClient

server = 'DESKTOP-M86GRUG/SQLEXPRESS'
database = 'ULAANBAATAR'
mongo_uri = 'mongodb://localhost:27017/'
mongo_db = 'darhan' 
mongo_collection = 'employee'  

conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')

query = "SELECT * FROM EMPLOYEES"
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

mongo_data = list(collection.find())

if len(mongo_data) > 0:
    it_data = [doc for doc in mongo_data if 'IT' in doc.get('ХЭЛТЭС', '')]

    conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
    cursor = conn.cursor()
    delete_query = "DELETE FROM EMPLOYEES WHERE ID IN ({})".format(','.join(str(row['ID']) for row in it_data))
    cursor.execute(delete_query)
    conn.commit()
    conn.close()

client.close()
