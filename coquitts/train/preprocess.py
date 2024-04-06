import os
import gc
import pandas
import traceback
from tqdm import tqdm

def format_audio_list(audio_files, number_of_audios, audio_transcriptions, out_path=None, eval_percentage=0.15, speaker_name='speaker'):
    
    txt_file = open(audio_transcriptions, 'r')
    
    files = []
    for i in range(1, number_of_audios + 1):
      files.append(audio_files + f'{i}.wav')
    
    audio_total_size: int = 0
    # make sure that ooutput file exists
    os.makedirs(out_path, exist_ok=True)

    metadata = {"audio_file": [], "text": [], "speaker_name": []}

    tqdm_object = tqdm(files)

    for audio_path in tqdm_object:

        sentence = txt_file.readline().split('|')[-1]
        sentence = sentence.removesuffix('\n')

        metadata["audio_file"].append(audio_path)
        metadata["text"].append(sentence)
        metadata["speaker_name"].append(speaker_name)

    df = pandas.DataFrame(metadata)
    df = df.sample(frac=1)
    num_val_samples = int(len(df)*eval_percentage)

    df_eval = df[:num_val_samples]
    df_train = df[num_val_samples:]

    df_train = df_train.sort_values('audio_file')
    train_metadata_path: str = out_path + r"\\metadata_train.csv"
    df_train.to_csv(train_metadata_path, sep="|", index=False)

    eval_metadata_path: str = out_path + r"\\metadata_eval.csv"
    df_eval = df_eval.sort_values('audio_file')
    df_eval.to_csv(eval_metadata_path, sep="|", index=False)

    # deallocate VRAM and RAM
    del df_train, df_eval, df, metadata
    # garbage collection
    gc.collect()

    return train_metadata_path, eval_metadata_path, audio_total_size

def preprocess_dataset(audio_path: str, number_of_audios: int, audio_transcriptions: str, out_path: str, speaker_name: str):
  
  out_path += r'\\dataset'
  os.makedirs(out_path, exist_ok=True)
  
  if audio_path is None:
      return "You should provide one or multiple audio files! If you provided it, probably the upload of the files is not finished yet!", "", ""
  else:
      try:
          train_meta, eval_meta, _ = format_audio_list(audio_path, number_of_audios, audio_transcriptions=audio_transcriptions, out_path=out_path, speaker_name=speaker_name)
      except:
          traceback.print_exc()
          error = traceback.format_exc()
          return f"The data processing was interrupted due an error !! Please check the console to verify the full error message! \n Error summary: {error}", "", ""

  return "Dataset Processed!", train_meta, eval_meta