from flask import Flask
from flask import render_template
from pymongo.mongo_client import MongoClient
from flask import request
from bson import json_util
import json

def create_app():
    app = Flask(__name__)
    mongoClient = MongoClient("mongodb://mongo:27017")

    @app.route("/")
    def hello_world():
        return render_template("index.html")
    
    @app.route("/save", methods=["POST"])
    def save():
        cardList = request.data.decode("utf-8")
        # todo: sideboards are seperated with a newline, rn it goes in as a blank card
        cardList = cardList.strip().split("\n")
        
        json_card_list = process_card_list(cardList)

        cardList = {"cards": json_card_list}
        
        try:
            mongoClient.magic_randomizer.decks.insert_one(cardList) # collection.deeper_collection.insert_one(document)
            return "Deck Added successfully!", 200
        except Exception as e:
            result = e
            return "", 500
        
    @app.route("/load", methods=["GET"])
    def load():
        decks = mongoClient.magic_randomizer.decks.find()
        decks = list(decks)
        
        data = {"decks": decks}
        data = json.loads(json_util.dumps(data))
        return data, 200

    def process_card_list(cardList):
        """
        Processes the card list and returns a json format of cards
        """
        # TODO: Add error handling for invalid card list
        json_card_list = []
        for card in cardList:
            card = card.split(" ")
            card = {"count": card[0], "name": " ".join(card[1:])} # joins the name in case the card name has spaces
            json_card_list.append(card)
        return json_card_list
    
    return app

def launch():
    return create_app()

if __name__ == "__main__":
    app = launch()
    app.run(port=8000, host="0.0.0.0", debug=True)