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

client = MongoClient(mongo_uri)
db = client[mongo_db]
collection = db[mongo_collection]

data = df.to_dict(orient='records')

collection.insert_many(data)


print("Verifying data in MongoDB...")
client = MongoClient(mongo_uri)
db = client[mongo_db]
collection = db[mongo_collection]
mongo_data = list(collection.find())

if len(mongo_data) > 0:
    print("Data transfer to MongoDB successful. Checking data:")
    for document in mongo_data:
        print(document)
        
    print("Deleting transferred data from MSSQL server...")
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes;')
    cursor = conn.cursor()
    delete_query = "DELETE FROM EMPLOYEES WHERE ID IN ({})".format(','.join(str(row['ID']) for row in df.to_dict('records')))
    cursor.execute(delete_query)
    conn.commit()
    conn.close()
    print("Transferred data deleted from MSSQL server.")
else:
    print("No data found in MongoDB. Data transfer might have failed.")

print("Process completed.")
#1fdhf
client.close()
#18:22