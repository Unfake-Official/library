import os
import random
from audio_to_spectrogram import *

input_folder = r'/Users/u22142/Documents/VozesFalsas'
output_folder = r'/Users/u22142/Documents/Espectrogramas'
is_fake = True # true if the folder contains fake audios, otherwise false

n_audios = 1000

if __name__ == '__main__':
    for subdirectory_input, _, _, in os.walk(input_folder):
        if subdirectory_input != input_folder and not subdirectory_input.__contains__('wavs'):

            print(f'Processing in: {subdirectory_input}')

            speaker_name = '/' + subdirectory_input.split('/')[-1] + '_Spectrograms'
            subdirectory_output = output_folder + speaker_name

            os.makedirs(subdirectory_output, exist_ok=True)

            for ix, file_name in enumerate(os.listdir(subdirectory_input + ('/wavs' if not is_fake else '/'))):
                input_audio_file = subdirectory_input + ('/wavs/' if not is_fake else '/') + file_name
                output_image_file = subdirectory_output + f'/{ix+1}.png'

                audio_to_spectrogram(input_audio_file, output_image_file)
