from add_environment_sounds import add_environment_sounds
from add_noise import add_noise
from spectrograms.main import generate_spectrograms

input_folder = r'/Users/u22142/Documents/Espectrogramas'
output_folder = r'/Users/u22142/Documents/Espectrogramas_Noise'

input_spec_folder = r'/Users/u22142/Documents/VozesFalsas'
output_spec_folder = r'/Users/u22142/Documents/Espectrogramas'
is_fake = True # true if the folder contains fake audios, otherwise false

n_audios = 1000
noise_rate = 0.5
noise_percentage = 16.7

voice_booster = 7
noise_hinder = 7

voices_folder = '/Users/u22142/Documents/VozesFalsas'
noise_folder = '/Users/u22142/Documents/VozesFalsas/DanielRibeiro_M002_Fake'
output_environment_folder = '/Users/u22142/Documents/VozesFalsas_Environment'

# Get percentage of the original voices to change
percentage = 16.7

add_environment_sounds(voice_booster, noise_hinder, voices_folder, noise_folder, output_folder, percentage)
generate_spectrograms(input_spec_folder, output_spec_folder, is_fake)
add_noise(input_folder, output_folder, n_audios, noise_rate, noise_percentage)
