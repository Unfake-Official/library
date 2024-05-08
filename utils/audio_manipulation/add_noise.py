import numpy as np
import matplotlib.pyplot as plt
import os
import random
from generate_spectrograms import audio_to_spectrogram
import PIL.Image as img

# Define a function to add noise to the spectrogram
def add_spectrogram_noise(spectrogram, noise_level):
    # Generate random noise with the same shape as the spectrogram
    noise = np.random.normal(0, noise_level, spectrogram.shape)

    # Add the noise to the spectrogram
    noisy_spectrogram = spectrogram + noise

    # Clip values to stay within the valid range
    noisy_spectrogram = np.clip(noisy_spectrogram, np.min(spectrogram), np.max(spectrogram))

    return noisy_spectrogram

def noise_to_audio_spectrogram(D: np.ndarray, output_image_file, sr, noise_level):
    # Add noise to the original spectrogram
    noisy_D = add_spectrogram_noise(D, noise_level=noise_level)

    # Save the noisy spectrogram as an image file
    plt.imsave(output_image_file, noisy_D, cmap='gray')
    image = img.open(output_image_file)
    new_image = image.resize((256, 256))
    new_image.save(output_image_file)


input_folder = r"C:\Users\mcsgo\OneDrive\Documentos\VozesFalsas"
output_folder = r"C:\Users\mcsgo\OneDrive\Documentos\Espectrogramas_Noise"

n_spectrograms = 1000
noise_rate = 0.5
noise_percentage = 16.7

is_fake = True

def add_noise(input_folder, output_folder, n_spectrograms, noise_rate, noise_percentage):
    for subdirectory_input, _, _, in os.walk(input_folder):
        if subdirectory_input != input_folder:

            print(f'Processing in: {subdirectory_input}')

            speaker_name = subdirectory_input.split('\\' if '\\' in subdirectory_input else '/')[-1]
            subdirectory_output = os.path.join(output_folder, f'{speaker_name}_Noise')

            os.makedirs(subdirectory_output, exist_ok=True)

            spectrogram_list = os.listdir(subdirectory_input)
            sample = random.sample(spectrogram_list, int(n_spectrograms * noise_percentage / 100))

            for ix, file_name in enumerate(sample):
                input_audio_file = os.path.join(subdirectory_input, ('wavs' if not is_fake else ''), file_name)
                output_image_file = os.path.join(subdirectory_output, f'{ix+1}_noise.png')
                try:
                    signal, sr = audio_to_spectrogram(input_audio_file, output_image_file, save=False)
                    noise_to_audio_spectrogram(signal, output_image_file, sr, noise_rate)
                except:
                    continue

add_noise(input_folder, output_folder, n_spectrograms, noise_rate, noise_percentage)
