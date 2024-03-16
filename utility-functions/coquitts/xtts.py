# this code is based on ⓍTTS (CoquiTTS' Text-to-Speech model) documentation, available at https://docs.coqui.ai/en/latest/models/xtts.html#tts-api

import torch
from TTS.api import TTS

device = "cuda" if torch.cuda.is_available() else "cpu"

list = list()
for i in range(1, 201):
  list.append(f"wavs/{i}.wav")

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
tts.tts_to_file(text="No total, serão chamados vinte e seis mil candidatos", speaker_wav=list, language="pt", file_path="output/xtts1.wav")

# tts = TTS(model_name="voice_conversion_models/multilingual/vctk/freevc24", progress_bar=False).to(device)
# tts.voice_conversion_to_file(source_wav="wavs/1.wav", target_wav="audio_example.wav", file_path="xtts2.wav")

# tts = TTS("tts_models/pt/cv/vits")
# tts.tts_with_vc_to_file(
#     "No total, serão chamados vinte e seis mil candidatos.",
#     speaker_wav=list,
#     file_path="xtts3.wav"
# )