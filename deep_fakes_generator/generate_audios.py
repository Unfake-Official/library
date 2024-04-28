import os

from generate_audios_from_txt import generate_audios_from_txt


def generate_audios(input_folder: str, output_folder: str, model):
    print('Adding audios to list')
    speaker_audios = list()
    # iterates through the original audios folder and appends the inner files paths
    for file_name in os.listdir(os.path.join(input_folder, 'wavs')):
        speaker_audios.append(os.path.join(input_folder, 'wavs', file_name))

    print('Audios added successfully')

    print('Processing speaker')
    gpt_cond_latent, speaker_embedding = model.get_conditioning_latents(audio_path=speaker_audios)

    print('Speaker processed successfully')

    generate_audios_from_txt(os.path.join(input_folder, 'texts.txt'), gpt_cond_latent, speaker_embedding, output_folder, model)
