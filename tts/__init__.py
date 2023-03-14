import os


class generator:
    def __init__(self, text: str) -> None:
        self.input_text = text
        self.generated_text = self.generate()

    def generate(self) -> bytes:
        self.file_id = len(os.listdir('tts/sounds/')) + 1
        os.system(f'tts --text "{self.input_text}" --model_path tts/model.pth --encoder_path tts/SE_checkpoint.pth.tar --encoder_config_path tts/config_se.json --config_path tts/config.json --speakers_file_path tts/speakers.pth --speaker_wav tts/conditioning_audio.wav --out_path tts/sounds/sound-{self.file_id}.wav')
        
    def convert_numbers_to_string(self):
        #convert all number to string
        pass
    
