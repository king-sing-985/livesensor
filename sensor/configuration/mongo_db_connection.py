from dotenv import load_dotenv
import pymongo
from sensor.constant.database import DATABASE_NAME
import certifi
ca = certifi.where()
from sensor.constant.env_variable import MONGODB_URL_KEY
import os
import logging

load_dotenv()

class MongoDBClient:
    client = None

    def __init__(self, database_name=DATABASE_NAME)->None:
        try:
            if MongoDBClient is None:
                mongodb_url = os.getenv(MONGODB_URL_KEY)
                logging.info(f"Retrieved MONGODB URL: {mongodb_url} ")

                if "localhost" is mongodb_url:
                    MongoDBClient.client = pymongo.MongoClient(mongodb_url)
                else:
                    MongoDBClient.client = pymongo.MongoClient(mongodb_url,tlsCAFile=ca) #TLS/SSl

            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
                
        except Exception as e:
            logging.error(f"Error initialisng MongoDB Client: {e}")
            raise