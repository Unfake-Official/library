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


input_folder = r"D:\-- TCC --\Vozes\Originais"
output_folder = r"D:\-- TCC --\Vozes\Espectrogramas com Noise"

noise_rate = 0.5
noise_percentage = 16.7

def add_noise(input_folder, output_folder, noise_rate, noise_percentage):
    for subdirectory_input in os.listdir(input_folder):
        speaker_folder = os.path.join(input_folder, subdirectory_input)
        if os.path.isdir(speaker_folder):
            speaker_name = speaker_folder.split('\\' if '\\' in speaker_folder else '/')[-1]
            wavs_folder = os.path.join(speaker_folder, 'wavs')

            print(f'Processing in: {wavs_folder}')

            subdirectory_output = os.path.join(output_folder, f'{speaker_name}_Noise')
            os.makedirs(subdirectory_output, exist_ok=True)

            audios_list = os.listdir(wavs_folder)
            n_audios = len(audios_list)
            np.random.shuffle(audios_list)
            sample = random.sample(audios_list, int(n_audios * noise_percentage / 100))

            for ix, file_name in enumerate(sample):
                input_audio_file = os.path.join(wavs_folder, file_name)
                output_image_file = os.path.join(subdirectory_output, f'{ix+1}_noise.png')
                try:
                    signal, sr = audio_to_spectrogram(input_audio_file, output_image_file, save=False)
                    noise_to_audio_spectrogram(signal, output_image_file, sr, noise_rate)
                except:
                    continue


add_noise(input_folder, output_folder, noise_rate, noise_percentage)
