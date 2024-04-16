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


def audio_to_spectrogram(input_audio_file: str, output_image_file: str):
    hl = 1024 # number of samples per time-step in spectrogram
    hi = 256 # Height of image
    wi = 2048 # Width of image

    y, sr = librosa.load(input_audio_file, sr=None)
    window = y[0:wi*hl]

    # generate the mel spectrogram
    D = np.abs(librosa.stft(y))**2
    S = librosa.feature.melspectrogram(S=D, sr=sr)
    S = librosa.feature.melspectrogram(y=window, sr=sr, n_fft=hl*2, hop_length=hl, n_mels=hi, fmax=10000)
    S = librosa.power_to_db(S, ref=np.max)

    # plot_spectrogram(mel_spect, sr)
    plt.imsave(output_image_file, S, cmap='gray')
