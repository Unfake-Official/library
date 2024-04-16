import librosa
import librosa.display
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import soundfile as sf


# Carregar a imagem do espectrograma
# spectrogram_image = plt.imread('/Users/u22156/Downloads/5.png')

img = Image.open('/Users/u22156/Downloads/5.png')
data = np.asarray(img)


# Converter a imagem para um array numpy
# spectrogram_data = np.mean(spectrogram_image, axis=2)

# Converta o espectrograma de volta para áudio (como mostrado no exemplo anterior)
#spec_complex = np.abs(spectrogram_data) * np.exp(1j * np.angle(spectrogram_data))
#audio_signal = librosa.istft(spec_complex)

S = librosa.feature.inverse.mel_to_stft(data)
y = librosa.griffinlim(S)

sf.write('/Users/u22156/Documents/Teste spectrogramas/reconstructed.wav', y, 48000)
