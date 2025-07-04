import os
from pymongo import MongoClient

client = MongoClient(os.getenv("MONGODB_URL"))
db = client["sirafinder"]
users_col = db["users"]
jobs_col = db["jobs"]
