import os
import time
from falabrasil import create_audio_folder_and_move_files, unify_txt_files, rename_audio_files

root_folder = r'' # The folder container all the speakers voices folders

try:
    for subdirectory, _, _ in os.walk(root_folder):
        if subdirectory != root_folder:
            print(f'Processing in: {subdirectory}')

            create_audio_folder_and_move_files(subdirectory)

            audios_folder = os.path.join(subdirectory, 'wavs')
            rename_audio_files(audios_folder)

            unify_txt_files(subdirectory)

            time.sleep(1)

except Exception as error:
    print(f'An error ocurred during processing. Message: {error}.')
