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
        plt.imsave(output_image_file, C, cmap='gray')
        image = img.open(output_image_file)
        new_image = image.resize((256, 256))
        new_image.save(output_image_file)

    return C, sr


input_folder = r"C:\Users\mcsgo\OneDrive\Documentos\ASVSPOOF\PA\PA\ASVspoof2019_PA_eval\flac"
output_folder = r"C:\Users\mcsgo\OneDrive\Documentos\ASVSPOOFSPEC\ASVspoof2019_PA_eval_Spectrograms"
var = "eval"


def generate_spectrograms(input_folder, output_folder):
    for ix, file_name in enumerate(os.listdir(input_folder)):
        input_audio_file = os.path.join(input_folder, file_name)
        output_image_file = os.path.join(output_folder, f'{ix+1}_{var}.png')

        audio_to_spectrogram(input_audio_file, output_image_file)


if __name__ == '__main__':
    generate_spectrograms(input_folder, output_folder)
