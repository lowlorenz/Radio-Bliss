import os

from flask import Flask, request, jsonify, send_file
from dotenv import load_dotenv
from pathlib import Path

from tts import TTS
from wiki import WikiParser
from route import get_route, get_point


dotenv_path = Path("../.env")
load_dotenv(dotenv_path=dotenv_path)
elevenlabs_api_key = os.getenv("ELEVENLABS_KEY")


route = None
app = Flask(__name__)


@app.route("/location", methods=["GET"])
def location():
    start_long = float(request.args.get("start_long"))
    start_lat = float(request.args.get("start_lat"))

    destination_long = float(request.args.get("destination_long"))
    destination_lat = float(request.args.get("destination_lat"))

    traveled_distance = float(request.args.get("distance"))

    route = get_route((start_long, start_lat), (destination_long, destination_lat))

    lat, long = get_point(route, distance=traveled_distance)

    return jsonify({"long": long, "lat": lat})


@app.route("/audioguide", methods=["GET"])
def audioguide():

    tts = TTS(elevenlabs_api_key)
    wiki = WikiParser()

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
