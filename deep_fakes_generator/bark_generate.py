import os
import time
import torch

from generate_audios import generate_audios

from TTS.tts.configs.bark_config import BarkConfig
from TTS.tts.models.bark import Bark

input_folder  = r'C:\Users\mcsgo\OneDrive\Documentos\Vozes'
output_folder = r'C:\Users\mcsgo\OneDrive\Documentos\VozesFalsas'

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

        config = BarkConfig()
        config.load_json(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json'))

        model = Bark.init_from_config(config)
        text_model_path = r"C:\Users\mcsgo\AppData\Local\tts\tts_models--multilingual--multi-dataset--bark\text_2.pt"
        coarse_model_path = r"C:\Users\mcsgo\AppData\Local\tts\tts_models--multilingual--multi-dataset--bark\coarse_2.pt"
        fine_model_path = r"C:\Users\mcsgo\AppData\Local\tts\tts_models--multilingual--multi-dataset--bark\fine_2.pt"
        hubert_model_path = r"C:\Users\mcsgo\AppData\Local\tts\tts_models--multilingual--multi-dataset--bark\hubert.pt"
        hubert_tokenizer_path = r"C:\Users\mcsgo\AppData\Local\tts\tts_models--multilingual--multi-dataset--bark\tokenizer.pth"
        model.load_checkpoint(config,
                              checkpoint_dir=r"C:\Users\mcsgo\AppData\Local\tts\tts_models--multilingual--multi-dataset--bark",
                              text_model_path=text_model_path,
                              coarse_model_path=coarse_model_path,
                              fine_model_path=fine_model_path,
                              hubert_model_path=hubert_model_path,
                              hubert_tokenizer_path=hubert_tokenizer_path)

        model.to(device)
        print('Model loaded successfully')

        os.makedirs(subdirectory_output, exist_ok=True)
        generate_audios(subdirectory_input, subdirectory_output, model)

# use the code below to download models

# # code from: https://docs.coqui.ai/en/latest/models/bark.html
# from TTS.api import TTS
# # C:\Users\mcsgo\AppData\Local\tts\tts_models--multilingual--multi-dataset--bark
# # tts_models/multilingual/multi-dataset/your_tts
# tts = TTS("tts_models/multilingual/multi-dataset/bark", gpu=True)
