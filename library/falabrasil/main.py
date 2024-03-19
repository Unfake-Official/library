import os
import time
from organizer.create_audio_folder_and_move_files import create_audio_folder_and_move_files
from organizer.unify_txt_files import unify_txt_files
from organizer.rename_audio_files import rename_audio_files

root_folder = '/Users/u22156/Documents/FalaBrasil/VozesV2'

if __name__ == '__main__':
    try:
        for subdirectory, _, _ in os.walk(root_folder):
            if subdirectory != root_folder:
                print(f'Processing in: {subdirectory}')

                create_audio_folder_and_move_files(subdirectory)

                audio_folder = os.path.join(subdirectory, 'wavs')
                rename_audio_files(audio_folder)

                unify_txt_files(subdirectory)

                time.sleep(1)

    except Exception as error:
        print(f'An error ocurred during processing. Message: {error}.')
    