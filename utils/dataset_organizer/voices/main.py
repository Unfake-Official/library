import os

folder = r"C:\Users\mcsgo\OneDrive\Documentos\TCC\Dataset\fake"

def rename(folder):
    w = os.walk(folder)
    for _, dirnames, _ in w:
        for d in dirnames:
            w = os.walk(os.path.join(folder, d))
            for _, _, filenames in w:
                for file in filenames:
                    old_path = os.path.join(os.path.join(folder, d), file)
                    new_path = os.path.join(os.path.join(folder, d), os.path.split(os.path.join(folder, d))[-1] + file)
                    os.rename(old_path, new_path)


if __name__ == '__main__':
    rename(folder)
