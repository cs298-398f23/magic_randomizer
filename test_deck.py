from deck import Deck
import pytest

def test_empty_deck():
    deck = Deck()
    assert deck.cards == []

def test_given_deck():
    deck = Deck(text="4 Brainstorm\n3 Consider\n4 Counterspell")
    assert deck.get_json() == {"cards": [{"count": "4", "name": "Brainstorm"}, {"count": "3", "name": "Consider"}, {"count": "4", "name": "Counterspell"}]}

def test_json_deck():
    deck = Deck(json=[{"count": "4", "name": "Brainstorm"}, {"count": "3", "name": "Consider"}, {"count": "4", "name": "Counterspell"}])
    assert deck.get_json() == deck.get_json() == {"cards": [{"count": "4", "name": "Brainstorm"}, {"count": "3", "name": "Consider"}, {"count": "4", "name": "Counterspell"}]}

def test_generate_card():
    deck = Deck()
    card = deck.generate_card("W")
    print(card)
    assert "W" in card["colors"]

def test_generate_decklist():
    deck = Deck(json={"cards": [{"count": "4", "name": "Brainstorm"}, {"count": "3", "name": "Consider"}, {"count": "4", "name": "Counterspell"}]})
    assert str(deck) == "4 Brainstorm\n3 Consider\n4 Counterspell"

def test_generate_deck():
    deck = Deck(generate=True, colors=["W"])
    assert len(deck.cards) == 11 # 10 unique cards + 1 land
    
    assert deck.cards[0]["name"] == "Plains"
    assert deck.cards[0]["count"] == 20

    assert deck.cards[1]["count"] == 4

def test_generate_deck_multiple_colors():
    deck = Deck(generate=True, colors=["W", "U"])
    assert len(deck.cards) == 12 # 10 unique cards + 2 land

    assert deck.cards[0]["name"] == "Plains"
    assert deck.cards[0]["count"] == 10

    assert deck.cards[1]["name"] == "Island"
    assert deck.cards[1]["count"] == 10

    assert deck.cards[2]["count"] == 4