import io
import os
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Form
from fastapi.responses import StreamingResponse
from TTS.utils.synthesizer import Synthesizer
from typing import Optional
import numpy as np
import soundfile as sf

class TTSResponse(BaseModel):
    status_code: int = 0
    error: Optional[str] = None

class TTSModel(BaseModel):
    MAX_TXT_LEN: int = int(os.getenv('TTS_MAX_TXT_LEN', 1000))
    SOUNDS_DIR: str = "sounds"
    MODEL_PATH: str = r"./model_files/model.pth"
    CONFIG_PATH: str = r"./model_files/config.json"
    SPEAKERS_PATH: str = r"./model_files/speakers.pth"
    ENCODER_CHECKPOINT_PATH: str = r"./model_files/SE_checkpoint.pth.tar"
    ENCODER_CONFIG: str = r"./model_files/config_se.json"
    SPEAKER_WAV: str = r"./model_files/conditioning_audio.wav"

# Initiate the model
engine_specs = TTSModel()

engine = Synthesizer(
    engine_specs.MODEL_PATH,
    engine_specs.CONFIG_PATH,
    tts_speakers_file=engine_specs.SPEAKERS_PATH,
    encoder_checkpoint=engine_specs.ENCODER_CHECKPOINT_PATH,
    encoder_config=engine_specs.ENCODER_CONFIG,
)

class Generator:
    def __init__(self, text: str) -> None:
        self.MAX_TXT_LEN = 1000
        self.SPEAKER_WAV = engine_specs.SPEAKER_WAV
        self.response = TTSResponse()
        self.audio_bytes = None
        self.audio_buffer = io.BytesIO()

        # Initiate the tts response
        if len(text) > self.MAX_TXT_LEN:
            text = text[: self.MAX_TXT_LEN]  # cut off text to the limit
            self.response.status_code = 10
            self.response.error = f"Input text was cutoff since it went over the {self.MAX_TXT_LEN} character limit."
        else:
            try:
                self.audio_bytes = engine.tts(text, speaker_wav=self.SPEAKER_WAV)
                self.save_audio()
            except Exception as e:
                self.response.status_code = 500
                self.response.error = str(e)

    def save_audio(self) -> None:
        # Ensure that all elements are converted to the correct type
        if isinstance(self.audio_bytes, list):
            self.audio_bytes = np.array(self.audio_bytes, dtype=np.float32)

        # Write the audio data to the BytesIO buffer as a WAV file
        sf.write(self.audio_buffer, self.audio_bytes, samplerate=22050, format='WAV')
        self.audio_buffer.seek(0)
