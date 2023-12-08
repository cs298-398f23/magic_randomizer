from flask import Flask
from flask import render_template
from pymongo.mongo_client import MongoClient
from flask import request
from bson import json_util
import json
from deck import Deck

def create_app():
    app = Flask(__name__)
    mongoClient = MongoClient("mongodb://mongo:27017")

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/save", methods=["POST"])
    def save():
        data = request.get_data().decode("utf-8")
        data = json.loads(data)
        deck = Deck(data["name"], text=data["deck_list"])
        try:
            # TODO: add check for duplicate name
            mongoClient.magic_randomizer.decks.insert_one(deck.get_json()) # collection.deeper_collection.insert_one(document)
            return "Deck Added successfully!", 200
        except Exception as e:
            result = e
            return str(result), 500

    @app.route("/load", methods=["GET"])
    def load():
        deck = mongoClient.magic_randomizer.decks.find({"name": request.args.get("name")})

        data = json.loads(json_util.dumps(deck))
        return data, 200

    @app.route("/random",methods=["GET"])
    def random():
        deck = Deck(generate=True, colors=request.args.get("colors").split(","))
        return str(deck), 200

    return app

def launch():
    return create_app()
