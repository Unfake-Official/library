import os
import shutil

original_path = '/Users/u22156/Downloads/Gabriela-200'


def organize_files_by_extension():
    audio_folder = os.path.join(original_path, 'wavs')
    transcriptions_folder = os.path.join(original_path, 'transcriptions')

    os.makedirs(audio_folder, exist_ok=True)
    os.makedirs(transcriptions_folder, exist_ok=True)

    for filename in os.listdir(original_path):
        file_path = os.path.join(original_path, filename)

        if os.path.isfile(file_path):
            name, extension = os.path.splitext(file_path)
            if extension.lower() == '.wav':
                shutil.move(file_path, audio_folder)
            elif extension.lower() == '.txt':
                shutil.move(file_path, transcriptions_folder)


organize_files_by_extension()
