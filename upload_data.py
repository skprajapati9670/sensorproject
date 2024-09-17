from pymongo.mongo_client import MongoClient
import pandas as pd
import json

url="mongodb+srv://skprajapati9670:hgH6EVVARiAXHnou@cluster1.uwu50.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"

client = MongoClient(url)
DATABASE_NAME="pwskills"

COLLECTION_NAME='waferfault'
df=pd.read_csv("E:\sensor project\notebooks\wafer_23012020_041211.csv")
df=df.drop("Unnamed: 0",axis=1)


json_record=list(json.loads(df.T.to_json()).values())