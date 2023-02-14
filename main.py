from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import FileResponse
from tts.generator import generator
from pydantic import BaseModel
import os
import aiofiles
from stt.transcribe import transcriber

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
async def transcribe_speech(audio_bytes: bytes = File()):
    speech  = transcriber(audio_bytes)

    return {"sentences": speech.transcription}

#Text to speech path
@api.post("/generate")
async def tts(request: Request, text : Text) -> str:
    text = text.dict()['text']
    file_id : int = len(os.listdir("TTS/sounds")) + 1
    #Infer the text
    os.system(f'tts --text "{text}" --model_path TTS/model.pth --encoder_path TTS/SE_checkpoint.pth.tar --encoder_config_path TTS/config_se.json --config_path TTS/config.json --speakers_file_path TTS/speakers.pth --speaker_wav TTS/conditioning_audio.wav --out_path TTS/sounds/sound-{file_id}.wav')
    return FileResponse(f"TTS/sounds/sound-{file_id}.wav", media_type="audio/wav")



