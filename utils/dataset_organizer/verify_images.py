from pathlib import Path
import imghdr
import shutil

data_dir = r'C:\Users\mcsgo\OneDrive\Documentos\TCC\Dataset2\real'
image_extensions = [".png"]

img_type_accepted_by_tf = ["bmp", "gif", "jpeg", "png"]
for filepath in Path(data_dir).rglob("*"):
    if filepath.suffix.lower() in image_extensions:
        img_type = imghdr.what(filepath)
        if img_type is None:
            print(f"{filepath} is not an image")
            shutil.move(filepath, r'C:\Users\mcsgo\OneDrive\Documentos\TCC\trash')
        elif img_type not in img_type_accepted_by_tf:
            print(f"{filepath} is a {img_type}, not accepted by TensorFlow")
