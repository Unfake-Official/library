import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

# Load the original audio file
audio_file = '/Users/u22156/Documents/spectrogram-noise-test/audio.wav'
y, sr = librosa.load(audio_file, sr=None)

# Generate the spectrogram
D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)

# Plot the original spectrogram
librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Original Spectrogram')
plt.show()
plt.imsave('/Users/u22156/Documents/spectrogram-noise-test/spectrogram.png', D, cmap='viridis')

# Define a function to add noise to the spectrogram
def add_spectrogram_noise(spectrogram, noise_level=0.5):
    # Generate random noise with the same shape as the spectrogram
    noise = np.random.normal(0, noise_level, spectrogram.shape)

    # Add the noise to the spectrogram
    noisy_spectrogram = spectrogram + noise

    # Clip values to stay within the valid range
    noisy_spectrogram = np.clip(noisy_spectrogram, np.min(spectrogram), np.max(spectrogram))

    return noisy_spectrogram

# Add noise to the original spectrogram
noisy_D = add_spectrogram_noise(D, noise_level=0.5)

# Plot the spectrogram with noise
librosa.display.specshow(noisy_D, sr=sr, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrogram with Noise')
plt.show()

# Save the noisy spectrogram as an image file
plt.imsave('/Users/u22156/Documents/spectrogram-noise-test/noisy_spectrogram.png', noisy_D, cmap='viridis')