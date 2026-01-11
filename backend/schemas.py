from pydantic import BaseModel
from typing import List

class TranscriptSegment(BaseModel):
    start: float
    end: float
    text: str


class TranscriptionResponse(BaseModel):
    segments: List[TranscriptSegment]
    total_segments: int
    duration: float
    eta_seconds: int
