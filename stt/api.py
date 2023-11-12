from fastapi import FastAPI, Request, File, WebSocket, Form, requests, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import os
from pymongo import MongoClient
from typing import Annotated

# Import packages
from transcribe import Transcriber
from utils.model_sdk import logger
from time import time
import json

# Import packages

#


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



class Text(BaseModel):
    text: str


class AudioBytes(BaseModel):
    data: bytes


@api.post(
    "/transcribe", tags=["Speech to Text", "Transcribe", "Speech Recognition", "STT"]
)
async def transcribe_speech(audio_bytes: bytes = File(...)) -> JSONResponse:
    # log the request
    log = logger(service="stt")

    # initiate the transcription
    speech = Transcriber(audio_bytes)

    # update the log
    log.update(total_words=len(speech.transcription.split(" ")), total_char=len(speech.transcription), text=speech.transcription, audio_size=len(audio_bytes))
    # commit the log
    log.commit_to_db()

    # return JSONResponse()
    return JSONResponse(
        content={
            "text": speech.transcription,
            "stats": log.log,
        }
    )


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


