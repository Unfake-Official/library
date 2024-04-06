import os
import torch
from TTS.api import TTS
from generate_audios_from_txt import generate_audios_from_txt

def generate_audios(input_folder: str, output_folder: str):
    speaker_voices = list()
    # iterates through the original audios folder and appends the inner files paths
    for file_name in os.listdir(input_folder + '/wavs'):
        speaker_voices.append(input_folder + '/wavs/' + file_name)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

    generate_audios_from_txt(input_folder + '/texts.txt', speaker_voices, output_folder, tts)
