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

def noise_to_audio_spectrogram(D: np.ndarray, output_image_file):
    # Add noise to the original spectrogram
    noisy_D = add_spectrogram_noise(D, noise_level=0.5)

    # Save the noisy spectrogram as an image file
    plt.imsave(output_image_file, noisy_D, cmap='viridis')
