from pathlib import Path
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    TEMP_DIR: str = "/tmp"
    MODEL_PATH: Path = Path("openai/whisper-small")
    ONNX_MODEL_PATH: Path = Path("/models/whisper-small.onnx")
    DEVICE: str = "cpu"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    @property
    def model_path_str(self) -> str:
        return str(self.MODEL_PATH)

    @property
    def onnx_model_path_str(self) -> str:
        return str(self.ONNX_MODEL_PATH)

settings = Settings()
