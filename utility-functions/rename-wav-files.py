import os

original_path = '/Users/u22156/Downloads/Gabriela-200/wavs'


def rename_wave_files():
    files = os.listdir(original_path)
    wav_files = [f for f in files if f.lower().endswith('.wav')]
    wav_files.sort()

    print(f'Wave files found: {str(len(wav_files))}')

    for index, wav_file in enumerate(wav_files, start=1):
        old_path = os.path.join(original_path, wav_file)
        new_path = os.path.join(original_path, f'{index}.wav')
        os.rename(old_path, new_path)


rename_wave_files()
