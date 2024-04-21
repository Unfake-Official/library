import os
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt


def plot_spectrogram(mel_spect: np.ndarray, sr: float):
    # Plot the original spectrogram
    librosa.display.specshow(mel_spect, y_axis='mel', fmax=8000, x_axis='time')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Original Spectrogram')
    plt.show()


def audio_to_spectrogram(input_audio_file: str, output_image_file: str, save: bool = True):
    hl = 1024 # number of samples per time-step in spectrogram
    hi = 256 # Height of image
    wi = 2048 # Width of image

    y, sr = librosa.load(input_audio_file, sr=None)
    window = y[0:wi*hl]

    # generate the mel spectrogram
    S = librosa.feature.melspectrogram(y=window, sr=sr, n_fft=hl*2, hop_length=hl, n_mels=hi, fmax=10000)
    S = librosa.power_to_db(S, ref=np.max)

    if save:
        # plot_spectrogram(mel_spect, sr)
        plt.imsave(output_image_file, S, cmap='gray')

    return S, sr


input_folder = r"C:\Users\mcsgo\OneDrive\Documentos\VozesFalsas"
output_folder = r"C:\Users\mcsgo\OneDrive\Documentos\Espectrogramas"
is_fake = True # true if the folder contains fake audios, otherwise false

def generate_spectrograms(input_folder, output_folder, is_fake):
    for subdirectory_input, _, _, in os.walk(input_folder):
        if subdirectory_input != input_folder and not subdirectory_input.__contains__('wavs'):

            print(f'Processing in: {subdirectory_input}')

            speaker_name = subdirectory_input.split('\\' if '\\' in subdirectory_input else '/')[-1] + '_Spectrograms'
            subdirectory_output = os.path.join(output_folder, speaker_name)

            os.makedirs(subdirectory_output, exist_ok=True)

            for ix, file_name in enumerate(os.listdir(os.path.join(subdirectory_input, ('wavs' if not is_fake else '')))):
                input_audio_file = os.path.join(subdirectory_input, ('wavs' if not is_fake else ''), file_name)
                output_image_file = os.path.join(subdirectory_output, f'{ix+1}.png')

                audio_to_spectrogram(input_audio_file, output_image_file)

generate_spectrograms(input_folder, output_folder, is_fake)
