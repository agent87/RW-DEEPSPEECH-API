import os
from pymongo import MongoClient
import pymongo
from pydantic import BaseModel
from datetime import datetime
import uuid
from time import time


client = MongoClient(
    f"mongodb://{os.getenv('MONGO_USERNAME')}:{os.getenv('MONGO_PASSWORD')}@{os.getenv('MONGO_HOST')}:{os.getenv('MONGO_PORT')}/"
)


class logger:
    log = {}

    def __init__(self, **kwargs) -> None:
        self.log["time"] = str(datetime.now().isoformat())
        self.log["feedback_token"] = str(uuid.uuid4())
        self.log["duration"] = time()

        for key, value in kwargs.items():
            self.log[key] = value

    async def commit_to_db(self):
        try:
            await client[os.getenv("MONGO_DATABASE")][
                os.getenv("MONGO_COLLECTION")
            ].insert_one(self.log)
        except pymongo.errors.ServerSelectionTimeoutError:
            pass

    def update(self, **kwargs):
        self.log["duration"] = time() - self.log["duration"]
        for key, value in kwargs.items():
            self.log[key] = value
