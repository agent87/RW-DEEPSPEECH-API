from TTS.utils.synthesizer import Synthesizer
import os
from pydantic import BaseModel


class tts_response(BaseModel):
    status_code: int = 10
    error: str = None


class TTS_MODEL(BaseModel):
    MAX_TXT_LEN: str = 1000  # os.getenv('TTS_MAX_TXT_LEN')
    SOUNDS_DIR: str = "sounds"
    MODEL_PATH: str = "./model.pth"
    CONFIG_PATH: str = "config.json"
    SPEAKERS_PATH: str = "speakers.pth"
    ENCODER_CHECKPOINT_PATH: str = "SE_checkpoint.pth.tar"
    ENCODER_CONFIG: str = "config_se.json"
    SPEAKER_WAV = "conditioning_audio.wav"



#Initiate the model
engine_specs = TTS_MODEL()

engine = Synthesizer(
            engine_specs.MODEL_PATH,
            engine_specs.CONFIG_PATH,
            tts_speakers_file=engine_specs.SPEAKERS_PATH,
            encoder_checkpoint=engine_specs.ENCODER_CHECKPOINT_PATH,
            encoder_config=engine_specs.ENCODER_CONFIG,
        )


class generator:
    MAX_TXT_LEN: str = 1000  # os.getenv('TTS_MAX_TXT_LEN')
    SOUNDS_DIR: str = "sounds"
    MODEL_PATH: str = "./model.pth"
    CONFIG_PATH: str = "config.json"
    SPEAKERS_PATH: str = "speakers.pth"
    ENCODER_CHECKPOINT_PATH: str = "SE_checkpoint.pth.tar"
    ENCODER_CONFIG: str = "config_se.json"
    SPEAKER_WAV = "conditioning_audio.wav"
    response = tts_response()

    def __init__(self, text) -> None:
        # Initiate the tts response
        if len(text) > self.MAX_TXT_LEN:
            text = text[: self.MAX_TXT_LEN]  # cut off text to the limit
            self.response.status_code = 10
            self.response.error = f"Input text was cutoff since it went over the {self.MAX_TXT_LEN} character limit."

        self.audio_bytes: bytes = engine.tts(
            text, speaker_wav=self.SPEAKER_WAV
        )

        # save the audio
        self.save_audio()

    

    def save_audio(self) -> str:
        file_id = len(os.listdir(self.SOUNDS_DIR)) + 1
        file_path = f"{self.SOUNDS_DIR}/sound-{file_id}.wav"

        with open(file_path, "wb+") as audio_file:
            engine.save_wav(self.audio_bytes, audio_file)

        self.file_path = file_path
