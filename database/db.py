from pymongo import MongoClient
import os


client=MongoClient(os.getenv("MONOGDB_URL"))
db=client["sirafinder"]
users_col=db["users"]
jobs_col=db["jobs"]


