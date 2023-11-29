from deck import Deck
import pytest

def test_empty_deck():
    deck = Deck()
    assert deck.cards == []

def test_given_deck():
    deck = Deck(text="4 Brainstorm\n3 Consider\n4 Counterspell")
    assert deck.cards == [{"count": "4", "name": "Brainstorm"}, {"count": "3", "name": "Consider"}, {"count": "4", "name": "Counterspell"}]

def test_json_deck():
    deck = Deck(json=[{"count": "4", "name": "Brainstorm"}, {"count": "3", "name": "Consider"}, {"count": "4", "name": "Counterspell"}])
    assert deck.get_json() == [{"count": "4", "name": "Brainstorm"}, {"count": "3", "name": "Consider"}, {"count": "4", "name": "Counterspell"}]