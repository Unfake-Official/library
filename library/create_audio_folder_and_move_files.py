import os
import shutil


def create_audio_folder_and_move_files(root_path: str):
    # create audio folder path
    audio_folder = os.path.join(root_path, 'wavs')
    os.makedirs(audio_folder, exist_ok=True)

    for filename in os.listdir(root_path):
        # iterate through each file in folder
        file_path = os.path.join(root_path, filename)

        if os.path.isfile(file_path):
            # get the extension if it's a file
            name, extension = os.path.splitext(file_path)
            if extension.lower() == '.wav':
                shutil.move(file_path, audio_folder)
