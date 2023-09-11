from TTS.utils.synthesizer import Synthesizer
import os
from pydantic import BaseModel


class tts_response(BaseModel):
    status_code : int = 10
    error : str = None


class generator:
    MAX_TXT_LEN : str = 1000#os.getenv('TTS_MAX_TXT_LEN')
    SOUNDS_DIR :str = "sounds"
    MODEL_PATH :str = "./model.pth"
    CONFIG_PATH :str = "config.json"
    SPEAKERS_PATH :str = "speakers.pth"
    ENCODER_CHECKPOINT_PATH :str = "SE_checkpoint.pth.tar"
    ENCODER_CONFIG :str = "config_se.json"
    SPEAKER_WAV= "conditioning_audio.wav"
    response = tts_response()


    def __init__(self, text) -> None:
        #Initiate the tts response
        if len(text) > self.MAX_TXT_LEN:
            text = text[:self.MAX_TXT_LEN] #cut off text to the limit
            self.response.status_code = 10
            self.response.error = f"Input text was cutoff since it went over the {self.MAX_TXT_LEN} character limit."
        
        self.audio_bytes : bytes = self.audio_synthesizer().tts(text, speaker_wav=self.SPEAKER_WAV)

        #save the audio
        self.save_audio()

    def audio_synthesizer(self):
        return Synthesizer(self.MODEL_PATH,
            self.CONFIG_PATH,
            tts_speakers_file=self.SPEAKERS_PATH,
            encoder_checkpoint=self.ENCODER_CHECKPOINT_PATH,
            encoder_config=self.ENCODER_CONFIG)

    def save_audio(self) -> str:
        file_id = len(os.listdir(self.SOUNDS_DIR)) + 1
        file_path = f"{self.SOUNDS_DIR}/sound-{file_id}.wav"

        with open(file_path, "wb+") as audio_file:
            self.audio_synthesizer().save_wav(self.audio_bytes, audio_file)

        self.file_path = file_path

