import asyncio, shutil, uuid, librosa
from pathlib import Path
from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware


from backend.audio_utils import convert_to_mp3
from backend.transcriber import transcribe_japanese
from backend.schemas import TranscriptionResponse, TranscriptSegment

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/transcribe", response_model=TranscriptionResponse)
async def transcribe(file: UploadFile):
    tmp_path = Path("uploads") / f"{uuid.uuid4()}_{file.filename}"
    with open(tmp_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    mp3_path = convert_to_mp3(tmp_path)

    loop = asyncio.get_running_loop()
    segments = await loop.run_in_executor(None, transcribe_japanese, mp3_path)

    duration = librosa.get_duration(path=str(mp3_path))

    payload = [
        TranscriptSegment(
            start=round(s["start"],2),
            end=round(s["end"],2),
            text=s["text"].strip()
        )
        for s in segments
    ]

    return TranscriptionResponse(
        segments=payload,
        total_segments=len(payload),
        duration=round(duration,2)
    )

@app.post("/export/srt")
async def export_srt(file: UploadFile):
    tmp_path = Path("uploads") / f"{uuid.uuid4()}_{file.filename}"
    with open(tmp_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    mp3_path = convert_to_mp3(tmp_path)
    loop = asyncio.get_running_loop()
    segments = await loop.run_in_executor(None, transcribe_japanese, mp3_path)

    srt = segments_to_srt(segments)
    return PlainTextResponse(srt, media_type="application/x-subrip")
