import os

from dotenv import load_dotenv
from pathlib import Path
from elevenlabs import generate, Voice, VoiceSettings, play


class TTS:

    def __init__(self, api_key):
        self.api_key = api_key
        self.voice = Voice(voice_id="2D055lf8hVKDhcLi4zij")  # Brian
        self.model = "eleven_turbo_v2"

    def tts(self, text):
        audio = generate(
            text=text, voice=self.voice, api_key=self.api_key, model=self.model
        )
        return audio


if __name__ == "__main__":

    dotenv_path = Path("../.env")
    load_dotenv(dotenv_path=dotenv_path)
    elevenlabs_api_key = os.getenv("ELEVENLABS_KEY")

    tts = TTS(api_key=elevenlabs_api_key)

    audio = tts.tts("Hello, world!")
    play(audio)
