import os
import random
from pydub import AudioSegment

voice_booster = 7 # Increases voice audio in 7db
noise_hinder = 7 # Decreases noise audio in 7db

voices_folder = r''
noise_folder  = r''
output_folder = r''

# Get percentage of the original voices to change
percentage = 16.7

def add_environment_sounds(voice_booster, noise_hinder, voices_folder, noise_folder, output_folder, percentage):
    # Get random noises to introduce into the audios
    environment_sounds = [audio for audio in os.listdir(noise_folder)]

    for subdirectory_input, _, _, in os.walk(voices_folder):
        if subdirectory_input != voices_folder and not subdirectory_input.__contains__('wavs'):
            print(f'Processing in: {subdirectory_input}')

            fake_audios = [audio for audio in os.listdir(subdirectory_input)]
            audios_to_change = int(len(fake_audios) * percentage / 100)
            audios = random.sample(fake_audios, audios_to_change)

            speaker_name = subdirectory_input.split('/')[-1]
            subdirectory_output = os.path.join(output_folder, speaker_name)

            os.makedirs(subdirectory_output, exist_ok=True)

            for ix, audio in enumerate(audios):
                noise = random.choice(environment_sounds)

                loaded_audio = AudioSegment.from_file(os.path.join(subdirectory_input, audio))
                loaded_noise = AudioSegment.from_file(os.path.join(noise_folder, noise))

                handled_audio = loaded_audio + voice_booster
                handled_noise = loaded_noise - noise_hinder

                overlayed = handled_audio.overlay(handled_noise)
                overlayed.export(os.path.join(subdirectory_output, f'{ix+1}.wav'), format='wav')


add_environment_sounds(voice_booster, noise_hinder, voices_folder, noise_folder, output_folder, percentage)
