from pydub import AudioSegment

voice_audio = AudioSegment.from_file('/Users/u22156/Documents/Teste ruidos/480.wav', format='wav')
noise = AudioSegment.from_file('/Users/u22156/Documents/Teste ruidos/thunderstorm.wav', format='wav')

voice_audio_louder = voice_audio + 7
noise_quieter = noise - 7

overlayed = voice_audio_louder.overlay(noise_quieter)

overlayed.export("/Users/u22156/Documents/Teste ruidos/overlayed.wav", format='wav')
