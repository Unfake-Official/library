from external import *

out_path = '/tmp/xtts_ft/'
num_epochs = 100
grad_acumm = 10
max_audio_length = 11
batch_size = 25
lang = 'pt'

n_audios = 1000
in_audio_path = 'C:\Users\mcsgo\OneDrive\Documentos\Vozes\AdrianaMalta_F049\wavs\\'
txt_path = 'C:\Users\mcsgo\OneDrive\Documentos\Vozes\AdrianaMalta_F049\\texts.txt'

out_audio_path = 'C:\Users\mcsgo\OneDrive\Documentos\VozesFalsas\AdrianaMalta_F049\wavs\\'

msg, train_meta, eval_meta = preprocess_dataset(in_audio_path, 1000, txt_path, lang, out_path, "AdrianaMalta")
print(msg)

msg, xtts_config, xtts_vocab, xtts_checkpoint, speaker_reference_audio = train_model(lang, train_meta, eval_meta, num_epochs, batch_size, grad_acumm, out_path, max_audio_length)

msg = load_model(xtts_checkpoint, xtts_config, xtts_vocab)
print(msg)

msg = run_tts(lang, txt_path, 1000, speaker_reference_audio, out_audio_path)
print(msg)