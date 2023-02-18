from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os
from datetime import datetime
from time import time
from pymongo import MongoClient
#Import packages
from stt.transcribe import transcriber
#from tts.generator import generator

import uuid



api = FastAPI()  #instance

##Mongo DB
class db_credentials(BaseModel):
    username : str = "myuser" #os.getenv('MONGO_USERNAME')
    password : str = "mypassword" #os.getenv('MONGO_PASSWORD')
    host : str = "locahost"#os.getenv('MONGO_HOST')
    port : str = "27017" #os.getenv('MONGO_PORT')
    database : str = "feedback" #os.getenv('MONGO_DATABASE')
    collection : str = "logs" #os.getenv("MONGO_COLLECTION")

db = db_credentials()

client = MongoClient(f'mongodb://{db.username}:{db.password}@{db.host}:{db.port}/')



class Text(BaseModel):
    text : str


class logger:
    log = {}
    def __init__(self, mode: str, ) -> None:
        self.log['mode'] = mode
        self.log['time'] = datetime.now()
        self.log['feedback_token'] = str(uuid.uuid4()) #client[db.database].list_collection_names(filter={'name': 'logs'})
        self.log['duration'] = time()


    def update(self, total_words:str = None, audio_size:int = None, file_name:str = None, text:str = None):
        self.log['duration'] = time() - self.log['duration']
        if total_words:
            self.log['total_words'] = total_words
        if audio_size:
            self.log['audio_size'] = audio_size
        if file_name:
            self.log['file_name'] = file_name
        if text:
            self.log['text'] = file_name

    def commit_to_db(self):
        client[db.database][db.collection].insert_one(self.log)



@api.post('/register') #route
def register(request: Request): #serving function
    return "User Registration Endpoint"


@api.post('/token') 
def get_token(request: Request):
    return "Here is your token"


@api.post("/transcribe")
async def transcribe_speech(audio_bytes: bytes = File()):
    #log the request
    #log =  logger("transcription")
    #initiate the transcription
    speech  = transcriber(audio_bytes)
    #update the log
    #log.update(total_words=len(speech.transcription), text=speech.transcription)
    #commit the log
    #log.commit_to_db()

    return {"sentences": speech.transcription}

#Text to speech path
@api.post("/generate_audio")
async def tts(request: Request, text : Text) -> str:
    text = text.dict()['text']
    file_id : int = len(os.listdir("tts/sounds")) + 1
    #Infer the text
    os.system(f'tts --text "{text}" --model_path tts/model.pth --encoder_path tts/SE_checkpoint.pth.tar --encoder_config_path tts/config_se.json --config_path tts/config.json --speakers_file_path tts/speakers.pth --speaker_wav tts/conditioning_audio.wav --out_path tts/sounds/sound-{file_id}.wav')
    return FileResponse(f"tts/sounds/sound-{file_id}.wav", media_type="audio/wav")



