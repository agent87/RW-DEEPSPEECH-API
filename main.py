from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import FileResponse
from tts.generator import generator
from pydantic import BaseModel

from stt.engine import transcriber

api = FastAPI()  #instance


class Text(BaseModel):
    text : str

@api.post('/register') #route
def register(request: Request): #serving function
    return "User Registration Endpoint"


@api.post('/token') 
def get_token(request: Request):
    return "Here is your token"


@api.post("/transcribe")
async def transcribe_speech(audio: bytes = File()):
    print(dir(audio))
    speech  = transcriber(audio)

    # Convert Speech to Text
    return {"sentences": "Sentences"}

@api.post('/generate')
def generate_speech(request: Request, text : Text):
    speech = generator(text)
    return FileResponse(f"tts/sounds/sound-{speech.file_id}.wav", media_type="audio/wav")



