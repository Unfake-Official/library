import os
import time

import torch

from create_audio_folder import create_audio_folder
from generate_audios import generate_audios

from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts

input_folder = r'C:\\Users\\mcsgo\\OneDrive\Documentos\\Vozes\\'
output_folder = r'C:\\Users\\mcsgo\\OneDrive\Documentos\\VozesFalsas\\'

if __name__ == '__main__':
    for subdirectory_input, _, _, in os.walk(input_folder):
        if subdirectory_input != input_folder and not subdirectory_input.__contains__('wavs'):
          print(f'Processing in: {subdirectory_input}')
          time.sleep(1)

          speaker_name = subdirectory_input.split('\\')[-1] + '_Fake'
          subdirectory_output = output_folder + speaker_name
          
          device = 'cuda' if torch.cuda.is_available() else 'cpu'
          
          # link to model: https://coqui.gateway.scarf.sh/hf-coqui/XTTS-v2/main/model.pth
          
          print('Loading model')
          
          config = XttsConfig()
          config.load_json(r'C:\\Users\\mcsgo\\OneDrive\Documentos\\GitHub\\unfake\\coquitts\working\\config.json')
          
          model = Xtts.init_from_config(config)
          model.load_checkpoint(config, checkpoint_dir=r'C:\\Users\\mcsgo\\OneDrive\Documentos\\GitHub\\unfake\\coquitts\working', vocab_path=r'C:\\Users\\mcsgo\\OneDrive\Documentos\\GitHub\\unfake\\coquitts\working\\vocab.json', use_deepspeed=False)
          
          model.to(device)
          print('Model loaded successfully')

          create_audio_folder(subdirectory_output)
          generate_audios(subdirectory_input, subdirectory_output, model)