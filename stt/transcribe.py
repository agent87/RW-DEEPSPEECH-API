import os
import nemo.collections.asr as nemo_asr
from pydub import AudioSegment
import pyaudioconvert as pac

#import the model using hugging face 
hf_model = nemo_asr.models.EncDecRNNTBPEModel.from_pretrained(model_name="mbazaNLP/Kinyarwanda_nemo_stt_conformer_model")



class transcriber:
    def __init__(self, audio_bytes : bytes) -> None:
        self.audio_bytes = audio_bytes

        #save the audio
        self.save_audio()

        #convert the audio file
        self.convert_wav_to_16bit_mono()

        #Transcribe
        self.transcription = self.transcribe()

    def save_audio(self):
        self.file_id = len(os.listdir('stt/sounds/'))
        with open(f"stt/sounds/sound-{self.file_id}.wav", "wb") as audio_file:
            audio_file.seek(0)
            audio_file.write(self.audio_bytes)


    def convert_wav_to_16bit_mono(self):
        try:
            file_path = f"stt/sounds/sound-{self.file_id}.wav"
            pac.convert_wav_to_16bit_mono(file_path,file_path)
            return True
        except FileNotFoundError:
            return False
        
    def transcribe(self):
        try:
            file_path = f"stt/sounds/sound-{self.file_id}.wav"
            result= hf_model.transcribe([file_path])
            return result[0]
        except FileNotFoundError:
            return "Unable to transcribe audio!"


