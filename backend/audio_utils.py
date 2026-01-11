import ffmpeg
import uuid
from pathlib import Path

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

def convert_to_mp3(input_path):
    out = UPLOAD_DIR / f"{uuid.uuid4()}.mp3"
    (
        ffmpeg
        .input(str(input_path))
        .output(str(out), ac=1, ar=16000)
        .run(quiet=True, overwrite_output=True)
    )
    return out
