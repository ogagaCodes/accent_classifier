import os

# work around multiple OpenMP runtimes being loaded
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
# pin OpenMP/MKL thread‐counts to 1 to save RAM/CPU
os.environ["OMP_NUM_THREADS"]   = "1"
os.environ["MKL_NUM_THREADS"]   = "1"

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from app.api.v1.analyze import router as analyze_router
from app.core.logging import setup_logging
from app.core.config import settings

setup_logging()
app = FastAPI(title="Video Accent Analyzer", version="1.0.0")

# === Add this block ===
app.add_middleware(
    CORSMiddleware,
    allow_origins=[ "https://d3ipbrrhsduo12.cloudfront.net/" ],   # React app’s URL
    allow_credentials=True,
    allow_methods=[ "GET", "POST", "OPTIONS" ],   # or ["*"] in dev
    allow_headers=[ "Content-Type", "Authorization" ],  # or ["*"]
)
# === end CORS block ===
app.include_router(analyze_router, prefix=settings.API_V1_STR)
handler = Mangum(app)
