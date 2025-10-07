from Card import Card

class Deck:
    def __init__(self, cards:list):
        self.cards = cards

    def __repr__(self):
        return f"Deck, {len(self.cards)} cards"

class DeckFactory:
    @staticmethod
    def generate_standard_deck():
        deck = Deck(
            cards = [Card(suit, face) for suit in Card.SUITS for face in Card.FACES.keys()]
        )

        return deck
