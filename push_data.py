import os
import sys
import json
import pandas as pd
from dotenv import load_dotenv
from pymongo import MongoClient
import certifi

# Custom imports
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging import logger

# Load environment variables
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print("Mongo URI:", MONGO_DB_URL)

ca = certifi.where()  # trusted certificate authority list

class NetworkDataExtract:
    def __init__(self):
        try:
            # You can add initialization logic here if needed
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def csv_to_json(self, file_path):
        """
        Convert CSV file to list of JSON-like Python dictionaries.
        """
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records  # <-- return the records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def insert_data_to_mongoDb(self, records, database, collection):
        """
        Insert the given records into the specified MongoDB collection.
        """
        try:
            client = MongoClient(MONGO_DB_URL, tls=True, tlsCAFile=ca)
            db = client[database]
            coll = db[collection]
            result = coll.insert_many(records)
            return len(result.inserted_ids)
        except Exception as e:
            raise NetworkSecurityException(e, sys)

if __name__ == "__main__":
    FILE_PATH = r"Network_Data\phisingData.csv"
    DATABASE = "CHARAN"
    COLLECTION = "Network_Data"

    networkobj = NetworkDataExtract()

    records = networkobj.csv_to_json(FILE_PATH)
    no_of_records = networkobj.insert_data_to_mongoDb(
        records=records,
        database=DATABASE,
        collection=COLLECTION
    )
    print(f"Number of records inserted to MongoDB is: {no_of_records}")
