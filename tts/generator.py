import os


class generate:
    sound_dir = "tts/sounds"
    file_id = len(os.listdir(sound_dir)) + 1

    
    def __init__(self, text: str) -> None:
        # Generate the audio file using the text-to-speech model
        os.system(f'tts --text "{text}" --model_path tts/model.pth --encoder_path tts/SE_checkpoint.pth.tar --encoder_config_path tts/config_se.json --config_path tts/config.json --speakers_file_path tts/speakers.pth --speaker_wav tts/conditioning_audio.wav --out_path {self.sound_dir}/sound-{self.file_id}.wav')

    @property
    def file_path(self) -> str:
        return str(self.sound_dir + self.file_id)
