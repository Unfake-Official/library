# this code is based on Bark (using CoquiTTS library) model documentation, available at https://docs.coqui.ai/en/latest/models/bark.html#example-use 

from TTS.api import TTS

tts = TTS("tts_models/multilingual/multi-dataset/bark")

tts.tts_to_file(text="Olá, meu nome é Ana Varela",
                file_path="bark1.wav",
                voice_dir="wavs/",
                speaker="ana_varela")