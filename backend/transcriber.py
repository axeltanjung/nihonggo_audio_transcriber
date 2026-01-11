import whisper

model = whisper.load_model("large-v3")

def transcribe_japanese(path):
    result = model.transcribe(str(path), language="ja", word_timestamps=True)
    return result["segments"]
