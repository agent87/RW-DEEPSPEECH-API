from fastapi import FastAPI, Request

api = FastAPI()  #instance

@api.post('/register') #route
def register(request: Request): #serving function
    return "User Registration Endpoint"


@api.post('/token') 
def get_token(request: Request):
    return "Here is your token"


@api.post('/stt')
def transcribe_speech(request: Request):
    #Convert Speech to Text
    return "Sentences"

@api.post('/tts')
def generate_speech(request: Request):
    #Generate Speech from text
    return "Audio Sound"



