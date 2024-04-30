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

print("Verifying data in MongoDB...")
mongo_data = list(collection.find())

if len(mongo_data) > 0:
    for document in mongo_data:
        print(document)
    
    it_data = [doc for doc in mongo_data if 'IT' in doc.get('ХЭЛТЭС', '')]
    for document in it_data:
        print(document)
    other_data_ids = [doc['_id'] for doc in mongo_data if 'IT' not in doc.get('ХЭЛТЭС', '')]
    result = collection.delete_many({'_id': {'$in': other_data_ids}})
    
else:
    print("No data found in MongoDB. Data transfer might have failed.")

client.close()

print("Process completed.")
