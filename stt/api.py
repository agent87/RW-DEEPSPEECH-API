from fastapi import FastAPI, Request, File, WebSocket, Form, requests, UploadFile
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os
from pymongo import MongoClient
from typing import Annotated
#Import packages
from transcribe import transcriber
import pymongo
from datetime import datetime
import uuid
from time import time
#Import packages





api = FastAPI(
    title="Speech to Text API",
    summary="A simple API that transcribes speech to text",
    version="1.0.1",
    contact={
        "name": "Arnaud Kayonga",
        "url": "http://kayarn.co/contact/",
        "email": "arnauldkayonga1@gmail.com",
    },
    license_info={
        "name": "GNU GENERAL PUBLIC LICENSE",
    },
)

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



class Text(BaseModel):
    text : str

class AudioBytes(BaseModel):
    data: bytes




@api.post("/transcribe")
async def transcribe_speech(audio_bytes: bytes = File(...), request: Request = Form(...)):
    #log the request
    log =  logger("stt", "http")
    #initiate the transcription
    audio = Request.form
    speech  = transcriber(audio_bytes)
    #update the log
    log.update(total_words=len(speech.transcription), text=speech.transcription)
    #commit the log
    log.commit_to_db(client)

    return {"sentences": speech.transcription}



# #WebSocket Section

# # @api.websocket("/ws/transcribe")
# # async def websocket_endpoint(websocket: WebSocket):
# #     await websocket.accept()
# #     while True:
# #         audio_bytes = await websocket.receive_json(AudioBytes)
# #         # Process the received audio bytes here
# #         # Example: write the audio bytes to a file
# #         with open("audio.wav", "ab") as f:
# #             f.write(audio_bytes.data)


# # @api.websocket("/ws/generate")
# # async def websocket_endpoint(websocket: WebSocket):
# #     """
# #     This function creates a WebSocket endpoint that accepts JSON messages containing a "text" field.
# #     If the length of the "text" field exceeds 50 characters, it sends a message back to the client indicating that the data is too large.
# #     Otherwise, it sends back the message text.
# #     """
# #     await websocket.accept()
# #     while True:
# #         try:
# #             data = await websocket.receive_json()
# #         except websocket.WebSocketDisconnect:
# #             break
# #         text = data.get("text", "")
# #         if len(text) > 50:
# #             await websocket.send_text("Data exceeds specified limit of 50 characters.")
# #         else:
# #             await websocket.send_text(f"Message text was: {text}")




