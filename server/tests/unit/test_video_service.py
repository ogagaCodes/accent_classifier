import pytest, os
from app.services.video_service import VideoService

def test_extract_audio(tmp_path, monkeypatch):
    dummy=tmp_path/'a.mp4'; dummy.write_bytes(b'')
    monkeypatch.setattr('subprocess.run', lambda *a,**k: open(str(dummy).replace('.mp4','.wav'),'wb').close())
    wav=VideoService().extract_audio(str(dummy))
    assert wav.endswith('.wav') and os.path.exists(wav)