import os


import os
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as img
from pydub import AudioSegment


def audio_to_spectrogram(input_audio_file: str, output_image_file: str, save: bool = True):
    audio = AudioSegment.from_file(input_audio_file)
    length = len(audio)
    # from 0 to 10 sec
    split_audio = audio[0: 10000 if length > 10000 else length]
    split_audio.export(input_audio_file)

    y, sr = librosa.load(input_audio_file)

    C = np.abs(librosa.cqt(y, sr=sr))
    C = librosa.amplitude_to_db(C, ref=np.max)

    if save:
        plt.imsave(output_image_file, C, cmap='viridis')
        image = img.open(output_image_file)
        new_image = image.resize((512, 256))
        new_image.save(output_image_file)

    return C, sr


input_folder = r"C:\Users\mcsgo\OneDrive\Documentos\TCC\VCTK-Corpus\VCTK-Corpus\wav48"
output_folder = r"C:\Users\mcsgo\OneDrive\Documentos\TCC\VCTK-Corpus-SPEC"


def generate_spectrograms(input_folder, output_folder):
    ix = 0
    for subdirectory_input, _, _, in os.walk(input_folder):
        if subdirectory_input != input_folder:

            print(f'Processing in: {subdirectory_input}')

            for file_name in os.listdir(subdirectory_input):
                ix += 1
                input_audio_file = os.path.join(subdirectory_input, file_name)
                output_image_file = os.path.join(output_folder, f'{ix+1}_vctk.png')

                try:
                    audio_to_spectrogram(input_audio_file, output_image_file)
                except:
                    continue


if __name__ == '__main__':
    generate_spectrograms(input_folder, output_folder)
