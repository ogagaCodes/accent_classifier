# import logging
# import os
# import onnxruntime as ort
# import numpy as np
# import soundfile as sf
# from transformers import WhisperProcessor
# from app.core.config import settings

# class TranscribeService:
#     logger = logging.getLogger(__name__)

#     def __init__(self):
#         # ALWAYS pass a plain str
#         self.proc = WhisperProcessor.from_pretrained(settings.model_path_str)

#         onnx_path = settings.onnx_model_path_str
#         if os.path.isfile(onnx_path):
#             self.sess = ort.InferenceSession(onnx_path)
#         else:
#             self.sess = None

#     def transcribe(self, audio_path: str) -> str:
#         if self.sess is None:
#             return ""
#         audio, sr = sf.read(audio_path)
#         inputs = self.proc(audio, sampling_rate=sr, return_tensors="np")
#         outputs = self.sess.run(None, {k: inputs[k] for k in inputs})
#         ids = np.argmax(outputs[0], axis=-1)
#         return self.proc.decode(ids[0]).strip()

# # Provider function:
# def get_transcribe_service() -> TranscribeService:
#     return TranscribeService()
import logging
import torch
import numpy as np
import soundfile as sf
from transformers import WhisperProcessor, WhisperForConditionalGeneration
from app.core.config import settings

class TranscribeService:
    logger = logging.getLogger(__name__)

    def __init__(self):
        model_name = "openai/whisper-tiny"
        # Load processor and model
        self.processor = WhisperProcessor.from_pretrained(model_name)
        self.model = WhisperForConditionalGeneration.from_pretrained(
            model_name,
            torch_dtype=torch.float16,
        ).to("cpu").eval()
        self.logger.info(f"Loaded Whisper model {model_name} on CPU in float16.")

    def transcribe(self, audio_path: str) -> str:
        # Read the WAV file
        audio, sr = sf.read(audio_path, dtype="float32")
        # Tokenize with explicit English translation task and return masks
        inputs = self.processor(
            audio,
            sampling_rate=sr,
            return_tensors="pt",
            return_attention_mask=True,
            language="en",    # force translation to English
            task="translate"  # ensure translate (not just transcription)
        )
        input_features = inputs.input_features.to(torch.float16)
        attention_mask = inputs.attention_mask

        # Prepare forced decoder ids for translation
        forced_decoder_ids = self.processor.get_decoder_prompt_ids(
            language="en",
            task="translate"
        )

        # Generate transcription/translation
        with torch.no_grad():
            generated_ids = self.model.generate(
                input_features,
                attention_mask=attention_mask,
                forced_decoder_ids=forced_decoder_ids
            )

        # Decode to text
        return self.processor.batch_decode(
            generated_ids,
            skip_special_tokens=True
        )[0].strip()

# Provider
def get_transcribe_service() -> TranscribeService:
    return TranscribeService()
