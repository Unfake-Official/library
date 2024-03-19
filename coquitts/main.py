import os
import time

from create_audio_folder import create_audio_folder
from generate_audios import generate_audios

input_folder = '/Users/u22142/Documents/Vozes'
output_folder = '/Users/u22142/Documents/VozesFalsas'

if __name__ == '__main__':
    try:
        for subdirectory_input, _, _, in os.walk(input_folder):
            if subdirectory_input != input_folder:
              print(f'Processing in: {subdirectory_input}')
              time.sleep(1)

              speaker_name = subdirectory_input.split('/')[-1] + '_Fake'
              subdirectory_output = output_folder + speaker_name

              create_audio_folder(subdirectory_output)
              generate_audios(subdirectory_input, subdirectory_output)
  
    except Exception as error:
      print(f'An error ocurred during processing. Message: {error}.')
