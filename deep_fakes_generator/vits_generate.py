import os
import time
import torch

from generate_audios import generate_audios

from TTS.tts.configs.vits_config import VitsConfig
from TTS.tts.models.vits import Vits

input_folder  = r'/Users/u22142/Documents/Vozes'
output_folder = r'/Users/u22142/Documents/VozesFalsas'

for subdirectory_input, _, _, in os.walk(input_folder):
    # For each speaker in input folder
    if subdirectory_input != input_folder and not subdirectory_input.__contains__('wavs'):
        print(f'Processing in: {subdirectory_input}')
        time.sleep(1)

        speaker_name = subdirectory_input.split('\\' if '\\' in subdirectory_input else '/')[-1] + '_Fake'
        subdirectory_output = os.path.join(output_folder, speaker_name)

        device = 'cuda' if torch.cuda.is_available() else 'cpu'

        print('Using', device)

        print('Loading model')

        config = VitsConfig()
        config.load_json(r'/Users/u22142/Library/Application Support/tts/tts_models--pt--cv--vits/config.json')

        model = Vits.init_from_config(config)
        model.load_checkpoint(config, r'/Users/u22142/Library/Application Support/tts/tts_models--pt--cv--vits/model_file.pth.tar')

        model.to(device)
        print('Model loaded successfully')

        model.format_batch()

        os.makedirs(subdirectory_output, exist_ok=True)
        generate_audios(subdirectory_input, subdirectory_output, model)

# # use the code below to download models

# from TTS.api import TTS

# # C:\Users\mcsgo\AppData\Local\tts\tts_models--ptl--cv--vits
# # tts_models/multilingual/multi-dataset/your_tts
# tts = TTS("tts_models/pt/cv/vits")
