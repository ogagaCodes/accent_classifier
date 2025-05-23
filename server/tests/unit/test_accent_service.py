import soundfile as sf
import numpy as np
from app.services.accent_service import AccentService

def test_accent(tmp_path):
    # soundfile only supports int16/int32/float32/float64
    arr = np.zeros(16000, dtype='int16')
    file=tmp_path/'t.wav'; sf.write(str(file),arr,16000)
    label,conf=AccentService().classify(str(file))
    assert isinstance(label,str) and isinstance(conf,float)