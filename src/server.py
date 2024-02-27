import os

from flask import Flask, request, jsonify, send_file
from dotenv import load_dotenv
from pathlib import Path

from tts import TTS
from wiki import WikiParser

dotenv_path = Path("../.env")
load_dotenv(dotenv_path=dotenv_path)
elevenlabs_api_key = os.getenv("ELEVENLABS_KEY")

app = Flask(__name__)
tts = TTS(elevenlabs_api_key)
wiki = WikiParser()


@app.route("/location", methods=["GET"])
def location():
    start_long = request.args.get("start_long")
    start_lat = request.args.get("start_lat")

    destination_long = request.args.get("destination_long")
    destination_lat = request.args.get("destination_lat")

    traveled_distance = request.args.get("distance")

    ...  # TODO load Minh Anh's code here
    # long, lat = get_location(start_city, destination_city, traveled_distance)
    long, lat = 50.1, 50.2

    return jsonify({"long": long, "lat": lat})


@app.route("/audioguide", methods=["GET"])
def audioguide():
    long = request.args.get("long")
    lat = request.args.get("lat")
    articles = wiki.get_articles(long, lat)
    ...  # TODO load Jonas' code here
    # text = llm.get_historical_anecdote(article)
    text = "hi"
    audio = tts.tts(text)

    with open("/tmp/output.mp3", "wb") as out:
        out.write(audio)

    return send_file("/tmp/output.mp3", mimetype="audio/mp3")
