import os
import pandas
import traceback
import torch
import torchaudio
from faster_whisper import WhisperModel
from tqdm import tqdm

out_path = '/tmp/xtts_ft/'
upload_file = 'folder/audio.wav'
lang = 'pt'

def format_audio_list(audio_files, target_language=lang, out_path=None, buffer=0.2, eval_percentage=0.15, speaker_name="coqui"):
    audio_total_size = 0
    # make sure that ooutput file exists
    os.makedirs(out_path, exist_ok=True)

    # Loading Whisper
    device = "cuda" if torch.cuda.is_available() else "cpu" 

    print("Loading Whisper Model!")
    asr_model = WhisperModel("large-v2", device=device, compute_type="float16")

    metadata = {"audio_file": [], "text": [], "speaker_name": []}

    tqdm_object = tqdm(audio_files)

    for audio_path in tqdm_object:
        wav, sr = torchaudio.load(audio_path)
        # stereo to mono if needed
        if wav.size(0) != 1:
            wav = torch.mean(wav, dim=0, keepdim=True)

        wav = wav.squeeze()
        audio_total_size += (wav.size(-1) / sr)

        segments, _ = asr_model.transcribe(audio_path, word_timestamps=True, language=target_language)
        segments = list(segments)
        i = 0
        sentence = ""
        sentence_start = None
        first_word = True
        # added all segments words in a unique list
        words_list = []
        for _, segment in enumerate(segments):
            words = list(segment.words)
            words_list.extend(words)

        # process each word
        for word_idx, word in enumerate(words_list):
            if first_word:
                sentence_start = word.start
                # If it is the first sentence, add buffer or get the begining of the file
                if word_idx == 0:
                    sentence_start = max(sentence_start - buffer, 0)  # Add buffer to the sentence start
                else:
                    # get previous sentence end
                    previous_word_end = words_list[word_idx - 1].end
                    # add buffer or get the silence midle between the previous sentence and the current one
                    sentence_start = max(sentence_start - buffer, (previous_word_end + sentence_start)/2)

                sentence = word.word
                first_word = False
            else:
                sentence += word.word

            if word.word[-1] in ["!", ".", "?"]:
                sentence = sentence[1:]
                # Expand number and abbreviations plus normalization
                sentence = multilingual_cleaners(sentence, target_language)
                audio_file_name, _ = os.path.splitext(os.path.basename(audio_path))

                audio_file = f"wavs/{audio_file_name}_{str(i).zfill(8)}.wav"

                # Check for the next word's existence
                if word_idx + 1 < len(words_list):
                    next_word_start = words_list[word_idx + 1].start
                else:
                    # If don't have more words it means that it is the last sentence then use the audio len as next word start
                    next_word_start = (wav.shape[0] - 1) / sr

                # Average the current word end and next word start
                word_end = min((word.end + next_word_start) / 2, word.end + buffer)
                
                absoulte_path = os.path.join(out_path, audio_file)
                os.makedirs(os.path.dirname(absoulte_path), exist_ok=True)
                i += 1
                first_word = True

                audio = wav[int(sr*sentence_start):int(sr*word_end)].unsqueeze(0)
                # if the audio is too short ignore it (i.e < 0.33 seconds)
                if audio.size(-1) >= sr/3:
                    torchaudio.save(absoulte_path,
                        audio,
                        sr
                    )
                else:
                    continue

                metadata["audio_file"].append(audio_file)
                metadata["text"].append(sentence)
                metadata["speaker_name"].append(speaker_name)

    df = pandas.DataFrame(metadata)
    df = df.sample(frac=1)
    num_val_samples = int(len(df)*eval_percentage)

    df_eval = df[:num_val_samples]
    df_train = df[num_val_samples:]

    df_train = df_train.sort_values('audio_file')
    train_metadata_path = os.path.join(out_path, "metadata_train.csv")
    df_train.to_csv(train_metadata_path, sep="|", index=False)

    eval_metadata_path = os.path.join(out_path, "metadata_eval.csv")
    df_eval = df_eval.sort_values('audio_file')
    df_eval.to_csv(eval_metadata_path, sep="|", index=False)

    # deallocate VRAM and RAM
    del asr_model, df_train, df_eval, df, metadata
    gc.collect()

    return train_metadata_path, eval_metadata_path, audio_total_size

def preprocess_dataset(audio_path, language, out_path):
  out_path = os.path.join(out_path, "dataset")
  os.makedirs(out_path, exist_ok=True)
  if audio_path is None:
      return "You should provide one or multiple audio files! If you provided it, probably the upload of the files is not finished yet!", "", ""
  else:
      try:
          train_meta, eval_meta, audio_total_size = format_audio_list(audio_path, target_language=language, out_path=out_path)
      except:
          traceback.print_exc()
          error = traceback.format_exc()
          return f"The data processing was interrupted due an error !! Please check the console to verify the full error message! \n Error summary: {error}", "", ""

  # if audio total len is less than 2 minutes raise an error
  if audio_total_size < 120:
      message = "The sum of the duration of the audios that you provided should be at least 2 minutes!"
      print(message)
      return message, "", ""

  print("Dataset Processed!")
  return "Dataset Processed!", train_meta, eval_meta