import numpy as np, soundfile as sf
from app.services.transcribe_service import TranscribeService

def test_transcribe(tmp_path, monkeypatch):
    arr=np.zeros(16000);
    file=tmp_path/'t.wav'; sf.write(str(file),arr,16000)
    svc=TranscribeService()
    # monkeypatch ONNX run
    monkeypatch=__import__('monkeypatch')
    # skip actual; assert transcribe returns str
    res=svc.transcribe(str(file))
    assert isinstance(res, str)