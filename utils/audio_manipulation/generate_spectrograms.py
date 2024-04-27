import os
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as img


def plot_spectrogram(mel_spect: np.ndarray, sr: float):
    # Plot the original spectrogram
    librosa.display.specshow(mel_spect, y_axis='mel', fmax=8000, x_axis='time')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Original Spectrogram')
    plt.show()


def audio_to_spectrogram(input_audio_file: str, output_image_file: str, save: bool = True):
    y, sr = librosa.load(input_audio_file)

    C = np.abs(librosa.cqt(y, sr=sr))
    C = librosa.amplitude_to_db(C, ref=np.max)

    if save:
        plt.imsave(output_image_file, C, cmap='gray')
        image = img.open(output_image_file)
        new_image = image.resize((256, 256))
        new_image.save(output_image_file)

    return C, sr


input_folder = r"C:\Users\mcsgo\OneDrive\Documentos\temp"
output_folder = r"C:\Users\mcsgo\OneDrive\Documentos\Espectrogramas"
is_fake = True  # true if the folder contains fake audios, otherwise false


def generate_spectrograms(input_folder, output_folder, is_fake):
    for subdirectory_input, _, _, in os.walk(input_folder):
        if subdirectory_input != input_folder and not subdirectory_input.__contains__('wavs'):

            print(f'Processing in: {subdirectory_input}')

            speaker_name = subdirectory_input.split(
                '\\' if '\\' in subdirectory_input else '/')[-1] + '_Spectrograms'
            subdirectory_output = os.path.join(output_folder, speaker_name)

            os.makedirs(subdirectory_output, exist_ok=True)

            for ix, file_name in enumerate(os.listdir(os.path.join(subdirectory_input, ('wavs' if not is_fake else '')))):
                input_audio_file = os.path.join(
                    subdirectory_input, ('wavs' if not is_fake else ''), file_name)
                output_image_file = os.path.join(
                    subdirectory_output, f'{ix+1}.png')

                audio_to_spectrogram(input_audio_file, output_image_file)


generate_spectrograms(input_folder, output_folder, is_fake)
