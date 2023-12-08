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

# def test_generate_card():
#     deck = Deck("test")
#     card = deck.generate_card("W")
#     print(card)
#     assert "W" in card["colors"]

def test_generate_decklist():
    deck = Deck("test", json=[{"count": "4", "name": "Brainstorm"}, {"count": "3", "name": "Consider"}, {"count": "4", "name": "Counterspell"}])
    assert str(deck) == "4 Brainstorm\n3 Consider\n4 Counterspell"

# def test_generate_deck():
#     deck = Deck("test", generate=True, colors=["W"])
#     assert len(deck.cards) == 11 # 10 unique cards + 1 land
    
#     assert deck.cards[0]["name"] == "Plains"
#     assert deck.cards[0]["count"] == 20

#     assert deck.cards[1]["count"] == 4

# def test_generate_deck_multiple_colors():
#     deck = Deck("test", generate=True, colors=["W", "U"])
#     assert len(deck.cards) == 12 # 10 unique cards + 2 land

#     assert deck.cards[0]["name"] == "Plains"
#     assert deck.cards[0]["count"] == 10

#     assert deck.cards[1]["name"] == "Island"
#     assert deck.cards[1]["count"] == 10

#     assert deck.cards[2]["count"] == 4

def test_throws_on_no_colors():
    with pytest.raises(Exception):
        deck = Deck("test", generate=True)

def test_deck_saves_name():
    deck = Deck(name="Test Deck")
    assert deck.name == "Test Deck"

def test_deck_json_to_json_has_name():
    deck = Deck(name="Test Deck", json=[{"count": "4", "name": "Brainstorm"}, {"count": "3", "name": "Consider"}, {"count": "4", "name": "Counterspell"}])
    assert deck.get_json()["name"] == "Test Deck"