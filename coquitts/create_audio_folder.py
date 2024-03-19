from coquitts import *

def create_audio_folder(folder:str, subdirectory:str):
    audio_folder = os.path.join(folder, subdirectory)
    os.makedirs(audio_folder, exist_ok=True)
