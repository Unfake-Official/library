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
    y, sr = librosa.load(input_audio_file, sr=None)
    # generate the mel spectrogram
    mel_spect = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=2048, hop_length=1024)
    mel_spect = librosa.power_to_db(mel_spect, ref=np.max)

    # plot_spectrogram(mel_spect, sr)
    plt.imsave(output_image_file, mel_spect, cmap='viridis')
