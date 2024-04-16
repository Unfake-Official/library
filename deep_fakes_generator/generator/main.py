'''
Link to pretrained portuguese model from CoquiTTS' Text-to-Speech: https://coqui.gateway.scarf.sh/hf-coqui/XTTS-v2/main/model.pth
'''
import os
import time
import torch

from generate_audios import generate_audios

from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts

input_folder  = r''
output_folder = r''

for subdirectory_input, _, _, in os.walk(input_folder):
    # For each speaker in input folder
    if subdirectory_input != input_folder and not subdirectory_input.__contains__('wavs'):
        print(f'Processing in: {subdirectory_input}')
        time.sleep(1)

        speaker_name = subdirectory_input.split('\\')[-1] + '_Fake'
        subdirectory_output = output_folder + speaker_name

        device = 'cuda' if torch.cuda.is_available() else 'cpu'

        print('Loading model')

        config = XttsConfig()
        config.load_json(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json'))

        model = Xtts.init_from_config(config)
        model.load_checkpoint(config, checkpoint_dir=os.path.dirname(os.path.abspath(__file__)), vocab_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vocab.json'), use_deepspeed=False)

        model.to(device)
        print('Model loaded successfully')

        os.makedirs(subdirectory_output, exist_ok=True)
        generate_audios(subdirectory_input, subdirectory_output, model)
