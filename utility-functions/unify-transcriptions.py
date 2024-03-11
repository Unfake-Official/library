import os

original_path = '/Users/u22156/Downloads/Gabriela-200/transcriptions'


def unify_txt_files(output_file):

    with open(output_file, 'w') as output_file:
        text_files = [file for file in os.listdir(original_path) if file.lower().endswith('.txt')]
        text_files.sort()

        for index, filename in enumerate(text_files, start=1):
            file_path = os.path.join(original_path, filename)

            if os.path.isfile(file_path):
                with open(file_path, 'r') as input_file:
                    content = input_file.read()
                    output_file.write(f'/content/TTS-TT2/wavs/{index}.wav|{content}')


# Replace 'your_folder_path' with the actual path to your folder containing .txt files
# Replace 'output.txt' with the desired name for the unified file
unify_txt_files(os.path.join(original_path, 'list.txt'))
