import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")

connection = MongoClient(MONGO_DB_URL)

conn = connection.free_cloud


