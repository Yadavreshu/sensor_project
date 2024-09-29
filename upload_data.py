from pymongo.mongo_client import MongoClient
import pandas as pd
import json

url = "mongodb+srv://reshu:V123456@cluster0.acxw0.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

DATABASE_NAME = "ORA"
COLLECTION_NAME = "waferfault"

df = pd.read_csv("/content/wafer_23012020_041211.csv")

df = df.drop("Unnamed:0",axis=1)

json_records =  list(json.loads(df.T.to_json()).values())


client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_records)





