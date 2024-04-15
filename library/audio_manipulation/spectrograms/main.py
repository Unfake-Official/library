import os
import random
from audio_to_spectrogram import *

input_folder = r'C:\\Users\\mcsgo\\OneDrive\Documentos\\Vozes\\'
output_folder = r'C:\\Users\\mcsgo\\OneDrive\Documentos\\Espectrogramas\\'

n_audios = 1000

if __name__ == '__main__':
    for subdirectory_input, _, _, in os.walk(input_folder):
        if subdirectory_input != input_folder and not subdirectory_input.__contains__('wavs'):
          
          print(f'Processing in: {subdirectory_input}')
          
          speaker_name = subdirectory_input.split('\\')[-1] + '_Spectrograms'
          subdirectory_output = output_folder + speaker_name
          
          os.makedirs(subdirectory_output, exist_ok=True)
          
          already_chose = []
          
          for ix, file_name in enumerate(os.listdir(input_folder + '/wavs')):
            input_audio_file = input_folder + '/wavs/' + file_name
            output_image_file = subdirectory_output + f'/{ix+1}.jpg'
                        
            audio_to_spectrogram(input_audio_file, output_image_file)
