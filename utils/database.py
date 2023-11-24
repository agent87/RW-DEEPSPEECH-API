import os
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError, OperationFailure
from pydantic import BaseModel
from datetime import datetime
import uuid
from time import time


client = MongoClient(
    f"mongodb://{os.getenv('MONGO_INITDB_ROOT_USERNAME')}:{os.getenv('MONGO_INITDB_ROOT_PASSWORD')}@{os.getenv('MONGO_HOST')}:{os.getenv('MONGO_PORT')}/"
)


class logger:
    log = {}

    def __init__(self, **kwargs) -> None:
        self.log["time"] = str(datetime.now().isoformat())
        self.log["feedback_token"] = str(uuid.uuid4())
        self.log["duration"] = time()

        for key, value in kwargs.items():
            self.log[key] = value

    def update(self, **kwargs):
        self.log["duration"] = time() - self.log["duration"]
        for key, value in kwargs.items():
            self.log[key] = value

    async def commit_to_db(self, collection):
        try:
            client[os.getenv("MONGO_INITDB_DATABASE")][os.getenv(f"{collection}")].insert_one(self.log)
            print("Log committed to database")
        except ServerSelectionTimeoutError as e:
            print("Could not connect to database")
            pass
        except OperationFailure as e:
            print("Could not commit log to database")
            pass
