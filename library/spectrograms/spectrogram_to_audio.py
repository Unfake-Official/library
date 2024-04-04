import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display

# Carregar a imagem do espectrograma
spectrogram_image = plt.imread('spectrogram_image.png')  # Substitua 'spectrogram_image.png' pelo nome do seu arquivo de imagem

# Converter a imagem para um array numpy
spectrogram_data = np.mean(spectrogram_image, axis=2)  # Converta para escala de cinza, se necessário

# Converta o espectrograma de volta para áudio (como mostrado no exemplo anterior)
spec_complex = np.abs(spectrogram_data) * np.exp(1j * np.angle(spectrogram_data))
audio_signal = librosa.istft(spec_complex)

# Reproduza o áudio ou salve-o em um arquivo
librosa.output.write_wav('reconstructed_audio.wav', audio_signal, sr)  # Altere 'sr' para a taxa de amostragem do seu áudio original, se necessário
