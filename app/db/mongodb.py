import os
from dotenv import load_dotenv
load_dotenv()

from pymongo.mongo_client import MongoClient

class Settings():

    MONGO_URI: str = os.environ['MONGO_URI']

    # Create a new client and connect to the server
    client = MongoClient(MONGO_URI)
    
    database = client["local"]

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print(f"Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
        
