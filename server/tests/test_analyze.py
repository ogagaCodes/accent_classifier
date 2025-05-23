import json

def test_analyze_endpoint(client, monkeypatch):
    monkeypatch.setattr('app.services.video_service.VideoService.download', lambda self,url: 'tests/test.mp4')
    monkeypatch.setattr('app.services.video_service.VideoService.extract_audio', lambda self,vid: 'tests/test.wav')
    monkeypatch.setattr('app.services.transcribe_service.TranscribeService.transcribe', lambda self,aud: 'hello world')
    monkeypatch.setattr('app.services.accent_service.AccentService.classify', lambda self,aud: ('British', 99.9))
    resp=client.post('/api/v1/analyze', json={'url':'http://x'})
    assert resp.status_code==200
    data=resp.json()
    assert data['accent']=='British'
    assert data['confidence']==99.9