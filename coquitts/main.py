from coquitts import *

from coquitts.create_audio_folder import create_audio_folder
from generate_audios import generate_audios

input_folder = '/Users/u22142/Documents/Vozes'
output_folder = 'Users/u22142/Documents/VozesFalsas'

if __name__ == '__main__':
    try:
        for subdirectory_input, _, _, in os.walk(input_folder):
            print(f'Processing in: {subdirectory_input}')
            time.sleep(1)

            subdirectory_output = subdirectory_input.split('/')[-1].join('_Fake')

            create_audio_folder(output_folder, subdirectory_output)
            generate_audios(subdirectory_input, subdirectory_output)
  
    except Exception as error:
      print(f'An error ocurred during processing. Message: {error}.')
