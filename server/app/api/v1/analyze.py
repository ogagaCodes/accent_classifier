import logging
from fastapi import APIRouter, Depends, HTTPException
from app.models.schemas import AnalyzeRequest, AnalyzeResponse
from app.services.video_service import VideoService
from app.services.transcribe_service import get_transcribe_service, TranscribeService
from app.services.accent_service import get_accent_service, AccentService

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze(
    req: AnalyzeRequest,
    video_svc: VideoService = Depends(),
    transcriber: TranscribeService = Depends(get_transcribe_service),
    classifier: AccentService = Depends(get_accent_service),
):
    try:
        logger.info(f"Received URL: {req.url}")
        video_path = await video_svc.download(str(req.url))
        audio_path = video_svc.extract_audio(video_path)

        transcription = transcriber.transcribe(audio_path)
        accent, confidence = classifier.classify(audio_path)
        summary = transcription[:200] + ("..." if len(transcription) > 200 else "")

        return AnalyzeResponse(
            accent=accent, confidence=confidence, summary=summary
        )
    except Exception as e:
        logger.error(f"Error during analysis: {e}")
        raise HTTPException(status_code=500, detail=str(e))
