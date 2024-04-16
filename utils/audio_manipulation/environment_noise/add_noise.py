import numpy as np
import matplotlib.pyplot as plt
import os
import random
import librosa

def spectrogram_to_audio(input_image_file: str):
  # Carregar a imagem do espectrograma
  spectrogram_image = plt.imread(input_image_file)  # Substitua 'spectrogram_image.png' pelo nome do seu arquivo de imagem

  # Converter a imagem para um array numpy
  spectrogram_data = np.mean(spectrogram_image, axis=2)  # Converta para escala de cinza, se necessário

  # Converta o espectrograma de volta para áudio (como mostrado no exemplo anterior)
  spec_complex = np.abs(spectrogram_data) * np.exp(1j * np.angle(spectrogram_data))
  audio_signal = librosa.istft(spec_complex)

  return audio_signal

# Define a function to add noise to the spectrogram
def add_spectrogram_noise(spectrogram, noise_level):
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


input_folder = r'C:\\Users\\mcsgo\\OneDrive\Documentos\\Spectrograms\\'
output_folder = r'C:\\Users\\mcsgo\\OneDrive\Documentos\\Spectrograms_Noise\\'

n_audios = 1000
noise_rate = 0.5
noise_percentage = 16.7

for subdirectory_input, _, _, in os.walk(input_folder):
  if subdirectory_input != input_folder:
    
    print(f'Processing in: {subdirectory_input}')
    
    speaker_name = subdirectory_input.split('\\')[-1] + '_Spectrograms'
    subdirectory_output = output_folder + speaker_name
    
    os.makedirs(subdirectory_output, exist_ok=True)
    
    audio_list = os.listdir(input_folder)
    sample = random.sample(audio_list, n_audios * noise_percentage / 100)
    
    for ix, file_name in enumerate(sample):
      input_image_file = input_folder + file_name
      output_image_file = output_folder + f'{ix+1}_noise.jpg'
      signal = spectrogram_to_audio(input_image_file)
      signal = add_spectrogram_noise(signal, noise_rate)
      noise_to_audio_spectrogram(signal, output_image_file)