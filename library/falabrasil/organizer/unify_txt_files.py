import os


def unify_txt_files(root_path: str):
    final_txt = os.path.join(root_path, 'texts.txt')
    # open final .txt file as write
    with open(final_txt, 'w') as final_txt:
        # get all .wav files and sort them by filename
        text_files = [file for file in os.listdir(root_path) if os.path.isfile(file) and file.lower().endswith('.txt')]
        text_files.sort()

        for index, filename in enumerate(text_files, start=1):
            text_file = os.path.join(root_path, filename)

            if os.path.isfile(text_file):
                with open(text_file, 'r') as input_file:
                    content = input_file.read()
                    final_txt.write(f'wavs/{index}.wav|{content}')
