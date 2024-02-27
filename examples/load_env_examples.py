from dotenv import load_dotenv
from pathlib import Path
import os

dotenv_path = Path("../.env")
load_dotenv(dotenv_path=dotenv_path)
elevenlabs_api_key = os.getenv("ELEVENLABS_KEY")

print(elevenlabs_api_key)
