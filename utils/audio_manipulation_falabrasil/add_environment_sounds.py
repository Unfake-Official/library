import os
import random
import numpy as np
from pydub import AudioSegment

voice_booster = 7 # Increases voice audio in 7db
noise_hinder = 7 # Decreases noise audio in 7db

voices_folder = r'D:\-- TCC --\Vozes\Originais'
noise_folder  = r'D:\-- TCC --\Ambient Noise\Noise'
output_folder = r'D:\-- TCC --\Vozes\Espectrogramas com Sons Ambiente'

# Get percentage of the original voices to change
percentage = 16.7

def add_environment_sounds(voice_booster, noise_hinder, voices_folder, noise_folder, output_folder, percentage):
    # Get random noises to introduce into the audios
    environment_sounds = [audio for audio in os.listdir(noise_folder)]

    for subdirectory_input in os.listdir(voices_folder):
        speaker_folder = os.path.join(voices_folder, subdirectory_input)
        if os.path.isdir(speaker_folder):
            speaker_name = speaker_folder.split('\\' if '\\' in speaker_folder else '/')[-1]
            wavs_folder = os.path.join(speaker_folder, 'wavs')

            subdirectory_output = os.path.join(output_folder, f'{speaker_name}_Environment')

            print(f'Processing in: {wavs_folder}')

            os.makedirs(subdirectory_output, exist_ok=True)

            audios_list = os.listdir(wavs_folder)
            n_audios = len(audios_list)
            np.random.shuffle(audios_list)
            sample = random.sample(audios_list, int(n_audios * percentage / 100))

            for ix, audio in enumerate(sample):
                noise = random.choice(environment_sounds)

                input_audio_file = os.path.join(wavs_folder, audio)
                input_noise_file = os.path.join(noise_folder, noise)

                loaded_audio = AudioSegment.from_file(input_audio_file, format='wav')
                loaded_noise = AudioSegment.from_file(input_noise_file, format='wav')

                handled_audio = loaded_audio + voice_booster
                handled_noise = loaded_noise - noise_hinder

                overlayed = handled_audio.overlay(handled_noise)
                overlayed.export(os.path.join(subdirectory_output, f'{ix+1}.wav'), format='wav')


if __name__ == '__main__':
    add_environment_sounds(voice_booster, noise_hinder, voices_folder, noise_folder, output_folder, percentage)
