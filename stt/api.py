from fastapi import FastAPI, File, Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import Annotated

# Import packages
from transcribe import Transcriber
from utils.database import logger

# Import packages




api = FastAPI(
    title="Speech to Text API",
    summary="A simple API that transcribes speech to text",
    version="1.0.1",
    contact={
        "name": "Arnaud Kayonga",
        "url": "https://www.kayarn.co",
        "email": "arnauldkayonga1@gmail.com",
    },
    license_info={"name": "GNU GENERAL PUBLIC LICENSE",},)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class Text(BaseModel):
    text: str


class AudioBytes(BaseModel):
    data: bytes


@api.post("/transcribe", tags=["Speech to Text", "Transcribe", "Speech Recognition", "STT"])
async def transcribe_speech(audio_bytes: bytes = File(...)) -> JSONResponse:
    # log the request
    log = logger(service="stt")

    # initiate the transcription
    # try:
    speech = Transcriber(audio_bytes)
    # update the log
    log.update(total_words=len(speech.transcription.split(" ")), total_char=len(speech.transcription), text=speech.transcription, audio_size=len(audio_bytes))
    # commit the log
    await log.commit_to_db(collection="MONGO_STT_COLLECTION")


    return JSONResponse(
        status_code=200,
        content={
            "text": speech.transcription,
            "stats": 0#log.log,
        }
    )
    
    # except:
    #     return JSONResponse(
    #         status_code=500,
    #         content={
    #             "text": "Sorry, we could not transcribe your audio. Please try again",
    #             "stats": log.log,
    #         }
    #     )

    


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


