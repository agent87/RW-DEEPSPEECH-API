FROM python:3.10.9

WORKDIR /API

COPY . .

RUN git clone https://huggingface.co/DigitalUmuganda/Kinyarwanda_YourTTS tts

RUN mkdir tts/sounds

RUN mkdir stt/sounds

RUN pip install -r requirements.txt

CMD uvicorn main:api --host=127.0.0.1 --port=8000 --reload
