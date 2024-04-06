import os
import torch
import torchaudio

from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts

XTTS_MODEL = None
def load_model(xtts_checkpoint: str, xtts_config: str, xtts_vocab: str):
    global XTTS_MODEL
    if not xtts_checkpoint or not xtts_config or not xtts_vocab:
        return "You need to run the previous steps or manually set the `XTTS checkpoint path`, `XTTS config path`, and `XTTS vocab path` fields !!"
    config = XttsConfig()
    config.load_json(xtts_config)
    XTTS_MODEL = Xtts.init_from_config(config)
    print("Loading XTTS model! ")
    XTTS_MODEL.load_checkpoint(config, checkpoint_path=xtts_checkpoint, vocab_path=xtts_vocab, use_deepspeed=False)

    return "Model Loaded!"

def run_tts(lang, tts_texts, number_of_audios, speaker_audio_file, output_path):
    if XTTS_MODEL is None or not speaker_audio_file:
        return "You need to run the previous step to load the model !!", None, None

    os.makedirs(output_path, exist_ok=True)
    file = open(tts_texts, 'r')

    for i in range(number_of_audios):
        sentence = file.readline().split('|')[-1]
        sentence = sentence.removesuffix('\n')
        
        gpt_cond_latent, speaker_embedding = XTTS_MODEL.get_conditioning_latents(audio_path=speaker_audio_file, gpt_cond_len=XTTS_MODEL.config.gpt_cond_len, max_ref_length=XTTS_MODEL.config.max_ref_len, sound_norm_refs=XTTS_MODEL.config.sound_norm_refs)
        
        out = XTTS_MODEL.inference(
            text=sentence,
            language=lang,
            gpt_cond_latent=gpt_cond_latent,
            speaker_embedding=speaker_embedding,
            temperature=XTTS_MODEL.config.temperature, # Add custom parameters here
            length_penalty=XTTS_MODEL.config.length_penalty,
            repetition_penalty=XTTS_MODEL.config.repetition_penalty,
            top_k=XTTS_MODEL.config.top_k,
            top_p=XTTS_MODEL.config.top_p,
        )
        
        file_output_path = output_path + f'{i}.wav'
        
        out["wav"] = torch.tensor(out["wav"]).unsqueeze(0)
        torchaudio.save(file_output_path, out["wav"], 24000)

    return "Speech generated !"
