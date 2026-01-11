from pathlib import Path
import ffmpeg, uuid

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

def convert_to_mp3(input_path: str) -> Path:
    output = UPLOAD_DIR / f"{uuid.uuid4()}.mp3"

    (
        ffmpeg
        .input(str(input_path))
        .output(str(output), ac=1, ar=16000)
        .run(overwrite_output=True, quiet=True)
    )

    return output
