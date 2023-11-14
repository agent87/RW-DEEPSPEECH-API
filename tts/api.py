from fastapi import FastAPI, Request, File, WebSocket
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
import os
from pymongo import MongoClient
import pymongo
from datetime import datetime
import uuid
from time import time
#Import packages
from generator import Generator
from utils.model_sdk import logger




api = FastAPI()  #instance




class Text(BaseModel):
    text : str
 




@api.post("/generate")
async def tts(request: Request, text: Text) -> FileResponse:
    """
    This function generates an audio file from the given text using a text-to-speech model.
    The generated audio file is returned as a response.
    """
    # Initialize the logger
    log = logger(service="tts")

    # Extract the text from the input
    text = text.text

    # Generate the audio file using the text-to-speech model
    try:
        audio = Generator(text)
    except:
        return JSONResponse(status_code=500,
            content={
                "text": "Sorry, we could not generate audio from your text. Please try again",
                "stats": log.log,
            }
        )

    # Log the request and commit it to the database
    log.update(total_words=len(text), text=text)
    log.commit_to_db() #async function

    # Return the generated audio file as a response
    return FileResponse(audio.file_path, media_type="application/octet-stream", filename="audio.wav")



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




