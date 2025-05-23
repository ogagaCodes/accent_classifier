import logging
import numpy as np
import onnxruntime as ort
import soundfile as sf
import librosa

from transformers import Wav2Vec2FeatureExtractor
from app.core.config import settings

class AccentService:
    logger = logging.getLogger(__name__)

    def __init__(self):
        checkpoint = "dima806/english_accents_classification"
        self.feature_extractor = Wav2Vec2FeatureExtractor.from_pretrained(checkpoint)

        self.session = ort.InferenceSession(
            "app/models/accent_model.onnx",
            providers=["CPUExecutionProvider"]
        )

        self.id2label = {
            0: "Australian",
            1: "British",
            2: "Canadian",
            3: "Indian",
            4: "Irish",
            5: "Scottish",
            6: "SouthAfrican",
            7: "US"
        }

        self.min_samples = 16000  # 1 second minimum

    def _ensure_min_length(self, audio: np.ndarray) -> np.ndarray:
        if audio.shape[-1] < self.min_samples:
            pad_amount = self.min_samples - audio.shape[-1]
            audio = np.pad(audio, (0, pad_amount), mode="constant")
        return audio

    def classify(self, audio_path: str) -> tuple[str, float]:
        audio, sr = sf.read(audio_path)
        if sr != 16000:
            audio = librosa.resample(audio, orig_sr=sr, target_sr=16000)
            sr = 16000

        audio = self._ensure_min_length(audio)
        inputs = self.feature_extractor(audio, sampling_rate=sr, return_tensors="np")
        input_values = inputs["input_values"]

        # Run inference
        ort_inputs = {self.session.get_inputs()[0].name: input_values}
        ort_outputs = self.session.run(None, ort_inputs)
        logits = ort_outputs[0][0]

        probs = np.exp(logits) / np.sum(np.exp(logits))  # softmax
        idx = np.argmax(probs)
        confidence = round(probs[idx] * 100, 1)

        label = self.id2label.get(idx, "Unknown")
        return label, confidence

# Dependency provider
def get_accent_service() -> AccentService:
    return AccentService()
