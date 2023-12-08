import random
import time
import requests

class Deck:
    def __init__(self, name, text = None, json = None, generate=False, colors=[]) -> None:
        self.name = name
        
        if text:
            self.cards = self.process_card_list(text)
        elif json:
            self.cards = json
        elif generate:
            self.cards = self.generate(colors)
        else:
            self.cards = []

    def process_card_list(self, cardList):
        """
        Processes the card list and returns a json format of cards
        """
        # TODO: Add error handling for invalid card list
        # TODO: sideboards are seperated with a newline, rn it goes in as a blank card

        cardList = cardList.strip().split("\n")
        json_card_list = []
        for card in cardList:
            card = card.split(" ")
            card = {"count": card[0], "name": " ".join(card[1:])} # joins the name in case the card name has spaces
            json_card_list.append(card)
        return json_card_list

    def generate(self, colors=[], size=60, num_of_cards=[4]):
        """
        Generates a deck based on the settings given
        :param: colors, a list of colors to generate the deck with
        """
        if colors == []:
            raise Exception("No colors given")
       
        cards = []

        land_types = {
            "W": "Plains",
            "U": "Island",
            "B": "Swamp",
            "R": "Mountain",
            "G": "Forest"
        }
        
        num_of_lands = size // 3
        num_of_each_land = num_of_lands // len(colors)
        for color in colors:
            cards.append({"name": land_types[color], "count": num_of_each_land})

        # TODO: make this work for random card counts
        for _ in range((size - num_of_lands) // 4):
            card = self.generate_card(random.choice(colors))
            time.sleep(0.075)
            cards.append({"name": card["name"], "count": 4})

        return cards

    def generate_card(self, color):
        """
        Generates a card based on the settings given
        :param: colors, a list of colors to generate the card with
        """
        #TODO: make the colors actually work
        url = "https://api.scryfall.com/cards/random"
        query= {"q": fr'o:"{{{color}}}" OR m:{{{color}}}'}
        return requests.get(url, params=query).json()

    def get_json(self) -> dict:
        """
        Returns a json representation of the deck
        """
        return {"name": self.name, "cards": self.cards, "deck_list": str(self)}

    def __str__(self) -> str:
        """
        Returns a string representation of the deck
        """
        decklist = ""
        for card in self.cards:
            decklist += f"{card['count']} {card['name']}\n"
        return decklist.strip()

    