import os
from audio_to_spectrogram import audio_to_spectrogram

input_folder = r"C:\Users\mcsgo\OneDrive\Documentos\VozesFalsas"
output_folder = r"C:\Users\mcsgo\OneDrive\Documentos\Espectrogramas"
is_fake = True # true if the folder contains fake audios, otherwise false

def generate_spectrograms(input_folder, output_folder, is_fake):
    for subdirectory_input, _, _, in os.walk(input_folder):
        if subdirectory_input != input_folder and not subdirectory_input.__contains__('wavs'):

            print(f'Processing in: {subdirectory_input}')

            speaker_name = subdirectory_input.split('\\')[-1] + '_Spectrograms'
            subdirectory_output = os.path.join(output_folder, speaker_name)

            os.makedirs(subdirectory_output, exist_ok=True)

            for ix, file_name in enumerate(os.listdir(os.path.join(subdirectory_input, ('wavs' if not is_fake else '')))):
                input_audio_file = os.path.join(subdirectory_input, ('wavs' if not is_fake else ''), file_name)
                output_image_file = os.path.join(subdirectory_output, f'{ix+1}.png')

                audio_to_spectrogram(input_audio_file, output_image_file)

generate_spectrograms(input_folder, output_folder, is_fake)
