from fastapi import FastAPI, Request, File, WebSocket
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os
from pymongo import MongoClient
#Import packages
from stt.transcribe import transcriber
from tts.generator import generator
from utils.model import logger




api = FastAPI()  #instance

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



class Text(BaseModel):
    text : str

class AudioBytes(BaseModel):
    data: bytes



@api.post('/register') #route
def register(request: Request): #serving function
    return "User Registration Endpoint"


@api.post('/token') 
def get_token(request: Request):
    return "Here is your token"


@api.post("/transcribe")
async def transcribe_speech(audio_bytes: bytes = File()):
    #log the request
    log =  logger("stt", "http")
    #initiate the transcription
    speech  = transcriber(audio_bytes)
    #update the log
    log.update(total_words=len(speech.transcription), text=speech.transcription)
    #commit the log
    log.commit_to_db(client)

    return {"sentences": speech.transcription}


@api.post("/generate")
async def tts(request: Request, text: Text) -> FileResponse:
    """
    This function generates an audio file from the given text using a text-to-speech model.
    The generated audio file is returned as a response.
    """
    # Initialize the logger
    log = logger("tts", "http")

    # Extract the text from the input
    text = text.text

    # Generate the audio file using the text-to-speech model
    audio = generator(text)

    # Log the request and commit it to the database
    log.update(total_words=len(text), text=text)
    log.commit_to_db(client)

    # Return the generated audio file as a response
    return FileResponse(audio.file_path, media_type="audio/wav")


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




