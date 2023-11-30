import requests

class Deck:
    def __init__(self, text = None, json = None) -> None:
        if text:
            self.cards = self.process_card_list(text)
        elif json:
            self.cards = json
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
        return {"cards": json_card_list}

    @staticmethod
    def generate(colors):
        """
        Generates a deck based on the settings given
        :param: colors, a list of colors to generate the deck with
        """
        pass

    def generate_card(self, color):
        """
        Generates a card based on the settings given
        :param: colors, a list of colors to generate the card with
        """
        #TODO: make the colors actually work
        url = "https://api.scryfall.com/cards/random"
        query= {"q": fr'o:"{color}" OR m:{color}'}
        return requests.get(url, params=query).json()

    def get_json(self) -> dict:
        """
        Returns a json representation of the deck
        """
        return self.cards
    
    def get_images() -> dict:
        """
        Returns a dict of images for the deck, the key is the card name and the value is the url of the image
        """
        pass

    