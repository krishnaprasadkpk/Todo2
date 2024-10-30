import certifi
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://krishnaprasad:kp12345@kp-coder.2bh5f.mongodb.net/?retryWrites=true&w=majority&appName=kp-coder"

# Create a new client and connect to the server
client = MongoClient(uri, ssl=True, tlsCAFile=certifi.where(), server_api=ServerApi('1'))


db = client.todo_db
collection = db["todo_data"]