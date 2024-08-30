import os
import shutil
import zipfile

dataset_dir = r"/Users/u22142/Documents/Dataset"

# dentro da pasta dataset:
# para cada pasta
# | para cada arquivo zip dentro da pasta
# | | descompactar arquivo na pasta com mesmo nome do arquivo zip
dirs = os.listdir(dataset_dir)
for d in dirs:
    label_dir = os.path.join(dataset_dir, d)
    if os.path.isdir(label_dir):
        zips = os.listdir(label_dir)
        for z in zips:
            zip_path = os.path.join(label_dir, z)
            if os.path.isfile(zip_path) and zipfile.is_zipfile(zip_path):
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(label_dir)

# dentro da pasta dataset:
# para cada pasta k
# | criar contador
# | para cada pasta descompactada
# | | para cada arquivo dentro da pasta
# | | | contador += 1
# | | | mover arquivo para pasta k e renomeá-lo com contador
dirs = os.listdir(dataset_dir)
for d in dirs:
    label_dir = os.path.join(dataset_dir, d)
    if os.path.isdir(label_dir):
        c = 0
        spec_dirs = os.listdir(label_dir)
        for sd in spec_dirs:
            sd_path = os.path.join(label_dir, sd)
            if os.path.isdir(sd_path):
                files = os.listdir(sd_path)
                for file in files:
                    file_path = os.path.join(sd_path, file)
                    shutil.move(file_path, label_dir)
                    new_file_path = os.path.join(label_dir, file)
                    c += 1
                    os.rename(new_file_path, os.path.join(label_dir, f"spec_{c}.png"))
