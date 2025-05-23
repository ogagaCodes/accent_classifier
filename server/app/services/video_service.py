import uuid
import subprocess
import aiohttp
from pathlib import Path
from app.core.config import settings
from yt_dlp import YoutubeDL

class VideoService:
    async def download(self, url: str) -> str:
        """
        Uses yt-dlp to grab the best MP4 (video+audio) from any public URL,
        writes it to a .mp4 in TEMP_DIR, and returns its path.
        """
        temp_dir = Path(settings.TEMP_DIR)
        temp_dir.mkdir(parents=True, exist_ok=True)
        out_path = temp_dir / f"{uuid.uuid4()}.mp4"

        # yt-dlp options: best mp4, write to our out_path
        ydl_opts = {
            "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",
            "outtmpl": str(out_path),
            "noplaylist": True,
            "quiet": True,
        }
        with YoutubeDL(ydl_opts) as ydl:
            # yt-dlp will raise on HTTP errors, etc.
            ydl.download([url])

        return str(out_path)

    def extract_audio(self, vid: str) -> str:
        """
        Runs ffmpeg to extract 16 kHz PCM WAV from the MP4.
        """
        vid_path = Path(vid)
        wav_path = vid_path.with_suffix(".wav")

        subprocess.run([
            "ffmpeg", "-y",
            "-i", str(vid_path),
            "-vn",
            "-acodec", "pcm_s16le",
            "-ar", "16000",
            str(wav_path)
        ], check=True)

        return str(wav_path)
