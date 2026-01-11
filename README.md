# 🎧 Japanese Audio Transcriber – ML Fullstack Project

Production-grade Japanese speech-to-text web application powered by Whisper large-v3 with timestamp segmentation and FFmpeg audio pipeline.

## Overview

This project provides an end-to-end audio/video → Japanese transcript pipeline with:

- Automatic video → MP3 conversion

- High-accuracy Whisper large-v3 ASR

- Sentence-level timestamps

- Clean web UI for uploading & viewing results

- Typed FastAPI backend with OpenAPI schema

- Designed as a real SaaS-like ML system, not a notebook demo.

## Architecture
User → Web UI → FastAPI API → FFmpeg Audio Pipeline → Whisper ASR → Timestamped Transcript
```
📁 Folder Structure
audio-transcriber/
│
├── backend/
│   ├── main.py
│   ├── transcriber.py
│   ├── audio_utils.py
│   ├── schemas.py
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
│
└── uploads/
```

## Installation
1. Clone repository
- git clone https://github.com/axeltanjung/nihonggo-audio-transcriber.git
- cd audio-transcriber

2. Setup Python environment
- python -m venv venv
- source venv/bin/activate   # Windows: venv\Scripts\activate
- pip install -r backend/requirements.txt

3. Install FFmpeg

OS	Command

Ubuntu	sudo apt install ffmpeg

Mac	brew install ffmpeg

Windows	Download from ffmpeg.org

▶ Run Application

Start Backend

uvicorn backend.main:app --reload


API will be available at:

http://localhost:8000/docs

Open Frontend

Simply open:

frontend/index.html


Upload audio/video and receive timestamped Japanese transcripts.

## API Response Example
```
{
  "segments": [
    {
      "start": 0.0,
      "end": 3.24,
      "text": "こんにちは、皆さん。"
    }
  ],
  "total_segments": 1,
  "duration": 3.24
}
```

## Key Engineering Highlights
Feature	Why it matters
Whisper large-v3	State-of-the-art ASR accuracy
FFmpeg pipeline	Handles any video/audio format
Typed Pydantic schemas	Stable, versionable API
Timestamp segmentation	Enables subtitles & indexing
Modular backend	Ready for microservice scaling
Clean frontend UI	Usable SaaS interface


## Resume Line

Built Japanese speech-to-text SaaS using Whisper large-v3 with timestamp segmentation, FFmpeg audio processing pipeline, and FastAPI backend.

## Roadmap

 Long-audio chunking & batching

 Subtitle (.srt) export

 Speaker diarization

 Real-time streaming mode

 Cloud deployment (GCP / HuggingFace Spaces)

## License

MIT License – free to use, extend, and commercialize.