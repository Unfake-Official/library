# this code is based on ⓍTTS (CoquiTTS' Text-to-Speech model) documentation, available at https://docs.coqui.ai/en/latest/models/xtts.html#tts-api
import os
from TTS.api import TTS


def generate_audios_from_txt(txt_file_path: str, speaker_voices: list, output_path: str, tts: TTS):
    if os.path.isfile(txt_file_path):
        with open(txt_file_path, 'r') as file:
            # removes the file path from the string, leaving only the audio transcription
            content = file.read().split('|')[-1]

            print(output_path)
            print(list)

            # generates the deep fake and stores it in output_path folder
            tts.tts_to_file(text=content, speaker_wav=speaker_voices, language="pt", file_path=output_path)
