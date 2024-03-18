import os
from organizer import unify_txt_files, rename_audio_files, create_audio_folder_and_move_files


root_folder = '/Users/u22156/Downloads/Gabriela-200'

if __name__ == '__main__':
    try:
        print(f'Processing in: {root_folder}')

        create_audio_folder_and_move_files(root_folder)

        audio_folder = os.path.join(root_folder, 'wavs')
        rename_audio_files(audio_folder)

        unify_txt_files(root_folder)

    except Exception as error:
        print(f'An error ocurred during processing. Message: {error}.')
    