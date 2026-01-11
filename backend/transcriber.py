import whisper
from pydub import AudioSegment

_model = None

def get_model():
    global _model
    if _model is None:
        _model = whisper.load_model("medium")
    return _model


def split_audio(path, chunk_ms=30_000):
    audio = AudioSegment.from_file(path)
    chunks = []
    for i in range(0, len(audio), chunk_ms):
        chunks.append(audio[i:i+chunk_ms])
    return chunks


def transcribe_japanese(path):
    model = get_model()
    print("🔊 Loading audio:", path)

    segments = []
    offset = 0.0

    for i, chunk in enumerate(split_audio(path)):
        print(f"⚙️  Processing chunk {i+1}")

        chunk_path = f"{path}_chunk.wav"
        chunk.export(chunk_path, format="wav")

        result = model.transcribe(chunk_path, language="ja", word_timestamps=True)

        print(f"✅ Finished chunk {i+1}")

        for s in result["segments"]:
            s["start"] += offset
            s["end"] += offset
            segments.append(s)

        offset += len(chunk) / 1000

    print("🏁 All chunks finished")
    return segments

