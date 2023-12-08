from deck import Deck
import pytest

def test_empty_deck():
    deck = Deck("test")
    assert deck.cards == []

def test_given_deck():
    deck = Deck("test", text="4 Brainstorm\n3 Consider\n4 Counterspell")
    assert deck.get_json() == {"name": "test",
                                "cards": [{"count": "4", "name": "Brainstorm"}, {"count": "3", "name": "Consider"}, {"count": "4", "name": "Counterspell"}], 
                                "deck_list": "4 Brainstorm\n3 Consider\n4 Counterspell"}

def test_json_deck():
    deck = Deck("test", json=[{"count": "4", "name": "Brainstorm"}, {"count": "3", "name": "Consider"}, {"count": "4", "name": "Counterspell"}])
    assert deck.get_json() == {"name": "test",
                                "cards": [{"count": "4", "name": "Brainstorm"}, {"count": "3", "name": "Consider"}, {"count": "4", "name": "Counterspell"}], 
                                "deck_list": "4 Brainstorm\n3 Consider\n4 Counterspell"}

def test_generate_deck():
    deck = Deck("test", generate=True)
    assert deck.get_json()["name"] == "test"
    assert len(deck.get_json()["cards"]) == 15

def test_generate_decklist():
    deck = Deck("test", json=[{"count": "4", "name": "Brainstorm"}, {"count": "3", "name": "Consider"}, {"count": "4", "name": "Counterspell"}])
    assert str(deck) == "4 Brainstorm\n3 Consider\n4 Counterspell"

def test_deck_saves_name():
    deck = Deck(name="Test Deck")
    assert deck.name == "Test Deck"

def test_deck_json_to_json_has_name():
    deck = Deck(name="Test Deck", json=[{"count": "4", "name": "Brainstorm"}, {"count": "3", "name": "Consider"}, {"count": "4", "name": "Counterspell"}])
    assert deck.get_json()["name"] == "Test Deck"