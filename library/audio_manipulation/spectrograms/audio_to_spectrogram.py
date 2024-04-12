import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt


# Define a function to add noise to the spectrogram
def add_spectrogram_noise(spectrogram, noise_level=0.5):
    # Generate random noise with the same shape as the spectrogram
    noise = np.random.normal(0, noise_level, spectrogram.shape)

    # Add the noise to the spectrogram
    noisy_spectrogram = spectrogram + noise

    # Clip values to stay within the valid range
    noisy_spectrogram = np.clip(noisy_spectrogram, np.min(spectrogram), np.max(spectrogram))

    return noisy_spectrogram


def plot_spectrogram(D: np.ndarray, sr: float):
    # Plot the original spectrogram
    librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Original Spectrogram')
    plt.show()


def audio_to_spectrogram(input_audio_file: str, output_image_file: str):
    y, sr = librosa.load(input_audio_file, sr=None)
    # Generate the spectrogram
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)

    # plot_spectrogram(D, sr)
    plt.imsave(output_image_file, D, cmap='viridis')


def noise_to_audio_spectrogram(D: np.ndarray, sr: float, output_image_file):
    # Add noise to the original spectrogram
    noisy_D = add_spectrogram_noise(D, noise_level=0.5)

    plot_spectrogram(noisy_D, sr)

    # Save the noisy spectrogram as an image file
    plt.imsave(output_image_file, noisy_D, cmap='viridis')
