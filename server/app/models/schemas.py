from pydantic import BaseModel, HttpUrl

class AnalyzeRequest(BaseModel):
    url: str

class AnalyzeResponse(BaseModel):
    accent: str
    confidence: float
    summary: str