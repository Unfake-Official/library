import os

def create_audio_folder(folder: str):
    os.makedirs(folder, exist_ok=True)
