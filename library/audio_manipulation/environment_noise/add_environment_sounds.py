import os
import random
from pydub import AudioSegment

voice_booster = 7
noise_hinder = 7

voices_folder = '/Users/u22156/Documents/Voice1/'
noise_folder = '/Users/u22156/Documents/Ruidos/'
output_folder = '/Users/u22156/Documents/Teste ruidos/output/'

# Get percentage of the original voices to change
percentage = 16.7

# Get random noises to introduce into the audios
environment_sounds = [audio for audio in os.listdir(noise_folder) if os.path.isfile(audio)]

for subdirectory_input, _, _, in os.walk(voices_folder):
    if subdirectory_input != voices_folder and not subdirectory_input.__contains__('wavs'):
        print(f'Processing in: {subdirectory_input}')

        fake_audios = [audio for audio in os.listdir(subdirectory_input) if os.path.isfile(audio)]
        audios_to_change = int(len(fake_audios) * percentage / 100)
        audios = random.sample(fake_audios, audios_to_change)

        for ix, audio in enumerate(audios):
            noise = random.choice(environment_sounds)

            loaded_audio = AudioSegment.from_file(os.path.join(subdirectory_input, audio), format='wav')
            loaded_noise = AudioSegment.from_file(os.path.join(noise_folder, noise), format='wav')

            handled_audio = loaded_audio + voice_booster
            handled_noise = loaded_noise - noise_hinder

            overlayed = handled_audio.overlay(handled_noise)
            overlayed.export(output_folder + f'/{ix+1}.wav', format='wav')
