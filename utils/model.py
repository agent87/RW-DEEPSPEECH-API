import os
from pymongo import MongoClient
import pymongo
from pydantic import BaseModel
from datetime import datetime
import uuid
from time import time

##Mongo DB
class db_credentials(BaseModel):
    username : str = os.getenv('MONGO_USERNAME')
    password : str = os.getenv('MONGO_PASSWORD')
    host : str = os.getenv('MONGO_HOST')
    port : str = os.getenv('MONGO_PORT')
    database : str = os.getenv('MONGO_DATABASE')
    collection : str = os.getenv("MONGO_COLLECTION")

db = db_credentials()

client = MongoClient(f'mongodb://{db.username}:{db.password}@{db.host}:{db.port}/')


class logger:
    log = {}
    def __init__(self, service: str, mode : str) -> None:
        self.log['service'] = service
        self.log['mode'] = mode
        self.log['time'] = datetime.now()
        self.log['feedback_token'] = str(uuid.uuid4()) 
        self.log['duration'] = time()

    def commit_to_db(self, client):
        try:
            client[db.database][db.collection].insert_one(self.log)
        except pymongo.errors.ServerSelectionTimeoutError:
            pass

    def update(self, total_words:str = None, audio_size:int = None, file_name:str = None, text:str = None):
        self.log['duration'] = time() - self.log['duration']
        if total_words:
            self.log['total_words'] = total_words
        if audio_size:
            self.log['audio_size'] = audio_size
        if file_name:
            self.log['file_name'] = file_name
        if text:
            self.log['text'] = text

    