'''
This code is based on ⓍTTS (CoquiTTS' Text-to-Speech model) documentation, available at:
https://docs.coqui.ai/en/latest/models/xtts.html#tts-api
'''
import os
import torch
import torchaudio
from tqdm import tqdm


def generate_audios_from_txt(txt_file_path: str, gpt_cond_latent, speaker_embedding, output_path: str, model):
    if os.path.isfile(txt_file_path):
        with open(txt_file_path, 'r', encoding='utf-8-sig') as file:
            data = file.readlines()

            print('Generating deepfakes')

            for ix, line in enumerate(tqdm(data)):
                # removes the file path from the string, leaving only the audio transcription
                content = line.split('|')[-1]

                output = os.path.join(output_path, f'{ix+1}_fake.wav')

                out = model.inference(
                    content,
                    'pt',
                    gpt_cond_latent,
                    speaker_embedding
                )
                torchaudio.save(output, torch.tensor(out['wav']).unsqueeze(0), 24000)

            print('Deepfakes generated successfully')
