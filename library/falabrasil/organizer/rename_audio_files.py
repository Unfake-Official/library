import os


def rename_audio_files(audios_folder_path: str):
    # get all .wav files and sort them by filename
    files = os.listdir(audios_folder_path)
    wav_files = [f for f in files if f.lower().endswith('.wav')]
    wav_files.sort()

    print(f'Wave files found: {str(len(wav_files))}')

    # for each one, create a new path with enumerate value and rename the file to the new path
    for index, wav_file in enumerate(wav_files, start=1):
        old_path = os.path.join(audios_folder_path, wav_file)
        new_path = os.path.join(audios_folder_path, f'{index}.wav')
        os.rename(old_path, new_path)
