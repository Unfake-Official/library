# this code is based on Bark (Suno's open-source text-to-speech model) documentation, available at https://github.com/suno-ai/bark?tab=readme-ov-file#-transformers-usage

from transformers import AutoProcessor, BarkModel

processor = AutoProcessor.from_pretrained("suno/bark")
model = BarkModel.from_pretrained("suno/bark")

voice_preset = "v2/pt_speaker_0"

inputs = processor("Meu nome é Marcos [laughs]", voice_preset=voice_preset)

audio_array = model.generate(**inputs)
audio_array = audio_array.cpu().numpy().squeeze()

from IPython.display import Audio

sample_rate = model.generation_config.sample_rate
Audio(audio_array, rate=sample_rate)

import scipy

sample_rate = model.generation_config.sample_rate
scipy.io.wavfile.write("output/audio.wav", rate=sample_rate, data=audio_array)