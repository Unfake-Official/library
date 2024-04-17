import librosa
import librosa.core
import librosa.core.spectrum
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import soundfile as sf
import scipy.signal
import scipy.io.wavfile


# Carregar a imagem do espectrograma
# spectrogram_image = plt.imread('/Users/u22156/Downloads/5.png')

img = Image.open('1.png')
i = np.asarray(img)


# Converter a imagem para um array numpy
# spectrogram_data = np.mean(spectrogram_image, axis=2)

# Converta o espectrograma de volta para áudio (como mostrado no exemplo anterior)
#spec_complex = np.abs(spectrogram_data) * np.exp(1j * np.angle(spectrogram_data))
#audio_signal = librosa.istft(spec_complex)

#wav = librosa.feature.inverse.mel_to_stft(i)
#print(wav)

#sf.write('meajuda.wav', np.ravel(wav), samplerate=48000)

audio = librosa.core.spectrum.griffinlim(i)
#scipy.io.wavfile.write('porfavor.wav', )
scipy.io.wavfile.write('test.wav', 48000, np.array(audio, dtype=np.int16))
#librosa.output.write_wav('test2.wav', audio, 48000)
sf.write('stereo_file.wav', audio, 48000)
