import os

from flask import Flask, request, jsonify, send_file
from dotenv import load_dotenv
from pathlib import Path
from llm import ChatGPT

from tts import TTS
from wiki import WikiParser
from route import get_route, get_point


dotenv_path = Path("../.env")
load_dotenv(dotenv_path=dotenv_path)
elevenlabs_api_key = os.getenv("ELEVENLABS_KEY")
openai_api_key = os.getenv("OPENAI")


route = None
app = Flask(__name__)
tts = TTS(elevenlabs_api_key)
wiki = WikiParser()
llm = ChatGPT(api_key=openai_api_key)


@app.route("/location", methods=["GET"])
def location():
    """
    params:
        start_long: float,
        start_lat: float,
        destination_long: float,
        destination_lat: float,
        distance: float
    return:
        (long: float, lat: float)
    """
    start = request.args.get("start")
    if not start:
        start_long = float(request.args.get("start_long"))
        start_lat = float(request.args.get("start_lat"))
        start = (start_long, start_lat)

    end = request.args.get("destination")
    if not end:
        destination_long = float(request.args.get("destination_long"))
        destination_lat = float(request.args.get("destination_lat"))
        end = (destination_long, destination_lat)

    traveled_distance = float(request.args.get("distance"))

    route = get_route(start, end)

    lat, long = get_point(route, distance=traveled_distance)

    results = jsonify({"long": long, "lat": lat})
    results.headers.add("Access-Control-Allow-Origin", "*")
    return results


@app.route("/funfacts", methods=["GET"])
def funfacts():
    """
    params:
        long: float,
        lat: float
    return:
        text: str
    """
    long = request.args.get("long")
    lat = request.args.get("lat")
    articles = wiki.get_articles(long, lat)
    text = llm.get_funfacts("".join(articles), 3)
    return jsonify({"text": text})


@app.route("/audioguide", methods=["GET"])
def audioguide():
    """
    params:
        long: float,
        lat: float
    return:
        mp3
    """

    tts = TTS(elevenlabs_api_key)
    wiki = WikiParser()

    long = request.args.get("long")
    lat = request.args.get("lat")
    articles = wiki.get_articles(long, lat)
    text = llm.get_funfacts("".join(articles), 3)
    audio = tts.tts(text)

    with open("/tmp/output.mp3", "wb") as out:
        out.write(audio)

    results = send_file("/tmp/output.mp3", mimetype="audio/mp3")
    results.headers.add("Access-Control-Allow-Origin", "*")
    return results
