import os
import shutil
import taglib

input_path = "/Users/u22156/Downloads/Gabriela-200/wavs"  # Add your path
output_path = "/Users/u22156/Downloads/Gabriela-200/output"  # Add your path


def update_metadata():
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for i in range(1, 201):  # change  this to the number of files in your folder + 1
        input_file = os.path.join(input_path, f"{i}.wav")
        output_file = os.path.join(output_path, f"{i}.wav")

        if os.path.exists(input_file):
            # Load WAV file and update metadata
            with taglib.File(input_file) as audio:
                # Set the title to match the file name without the extension
                audio.tags["TITLE"] = [f"{i}"]
                # Set the track number to match the file name without the extension
                audio.tags["TRACKNUMBER"] = [f"{i}"]

                # Save updated WAV file
                audio.save()

            # Copy the updated file to the output folder instead of moving it
            shutil.copy2(input_file, output_file)

            print(
                f"Updated metadata for {i}.wav: title='{i}', track number={i}")  # Update the print statement as well
        else:
            print(f"File {i}.wav not found.")



update_metadata()