from coquitts import *

from generate_audios_from_txt import generate_audios_from_txt

def generate_audios(input_folder: str, output_folder):
    speaker_voices = list()
    # iterates through the original audios folder and appends the inner files paths
    for filename in os.listdir(input_folder.join('/wavs')):
        speaker_voices.append(filename)

    generate_audios_from_txt(input_folder.join('/texts.txt'), speaker_voices, output_folder)