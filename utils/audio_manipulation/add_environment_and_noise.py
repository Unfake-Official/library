from add_environment_sounds import add_environment_sounds
from add_noise import add_noise
from generate_spectrograms import generate_spectrograms

voices_folder = r"C:\Users\mcsgo\OneDrive\Documentos\VozesFalsas"
noise_folder = r"C:\Users\mcsgo\OneDrive\Documentos\Noise"
output_environment_folder = r"C:\Users\mcsgo\OneDrive\Documentos\Environment"

output_spec_folder = r"C:\Users\mcsgo\OneDrive\Documentos\Espectrogramas"
is_fake = True # true if the folder contains fake audios, otherwise false

output_noise_folder = r"C:\Users\mcsgo\OneDrive\Documentos\Espectrogramas_Noise"

n_audios = 1000
noise_rate = 0.5
noise_percentage = 16.7

voice_booster = 7
noise_hinder = 7

# Get percentage of the original voices to change
percentage = 16.7

add_environment_sounds(voice_booster, noise_hinder, voices_folder, noise_folder, output_environment_folder, percentage)
generate_spectrograms(output_environment_folder, output_spec_folder, is_fake)
add_noise(output_spec_folder, output_noise_folder, n_audios, noise_rate, noise_percentage)
