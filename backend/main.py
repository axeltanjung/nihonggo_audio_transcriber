from fastapi import FastAPI, UploadFile
from audio_utils import convert_to_mp3
from transcriber import transcribe_japanese
import shutil, uuid
from schemas import TranscriptionResponse, TranscriptSegment
import whisper, librosa

app = FastAPI()

@app.post("/transcribe", response_model=TranscriptionResponse)
async def transcribe(file: UploadFile):
    ...

    segments = transcribe_japanese(mp3)
    duration = librosa.get_duration(path=mp3)

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