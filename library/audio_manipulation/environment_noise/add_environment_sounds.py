import os
import random
from pydub import AudioSegment

voice_booster = 7
noise_hinder = 7

voice_folder = '/Users/u22156/Documents/Teste ruidos/'
noise_folder = '/Users/u22156/Documents/Teste ruidos/'
output_folder = '/Users/u22156/Documents/Teste ruidos/output/'

# Get percentage of the original voices to change
percentage = 20
fake_audios = [audio for audio in os.listdir(voice_folder) if os.path.isfile(audio)]
audios_to_change = int(len(fake_audios) * percentage / 100)
audios = random.sample(fake_audios, audios_to_change)

# Get random noises to introduce into the audios
# Approach 1 - Get constant noises that don't change, that means it is a fixed portion of the noise dataset:
environment_sounds = [audio for audio in os.listdir(noise_folder) if os.path.isfile(audio)]
# if len(environment_sounds) > audios_to_change:
#     noises = random.sample(environment_sounds, audios_to_change)
# else:
#     noises = environment_sounds

# Approach 2 - Get a random noise for every audio:
for audio in audios:
    noise = random.choice(environment_sounds)

    loaded_audio = AudioSegment.from_file(os.path.join(voice_folder, audio), format='wav')
    loaded_noise = AudioSegment.from_file(os.path.join(noise_folder, noise), format='wav')

    handled_audio = loaded_audio + voice_booster
    handled_noise = loaded_noise + noise_hinder

    overlayed = handled_audio.overlay(handled_noise)
    overlayed.export(output_folder, format='wav')
