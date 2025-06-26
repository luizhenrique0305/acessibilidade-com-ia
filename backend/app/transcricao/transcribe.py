import openai
import os
from pydub import AudioSegment

def extrair_audio(video_path: str, audio_path: str = "audio.wav"):
    video = AudioSegment.from_file(video_path)
    video.export(audio_path, format="wav")
    return audio_path

def transcrever_audio(audio_path: str) -> str:
    openai.api_key = os.getenv("OPENAI_API_KEY")
    with open(audio_path, "rb") as f:
        transcript = openai.Audio.transcribe("whisper-1", f)
    return transcript["text"]
