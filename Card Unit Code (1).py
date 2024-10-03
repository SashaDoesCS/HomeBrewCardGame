##########################################[DEFINING CARD CLASS + EFFECTS]##########################################

class Card:
    def __init__(self, name, hp, atk, def_, mp):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.def_ = def_
        self.mp = mp
        self.is_disabled = False #Bard's doing

    def apply_effect(self, other_cards):
        if self.is_disabled:
            return
        if self.name == "Cleric":
            for card in other_cards:
                card.hp += 10
        elif self.name == "Paladin":
            for card in other_cards:
                card.atk += 10
        elif self.name == "Druid":
            for card in other_cards:
                card.def_ += 10
        elif self.name == "Elf":
            for card in other_cards:
                card.mp += 10
        # Bard's disabling effect is handled separately

    def disable(self):
        self.is_disabled = True

    def __str__(self):
        return f"{self.name}: HP={self.hp}, ATK={self.atk}, DEF={self.def_}, MP={self.mp}, Disabled={self.is_disabled}"

##########################################[INITIALIZING CARDS + DECK CREATION]##########################################
def create_deck():
    deck = []
    card_specs = [
        ("Elf", 15, 10, 8, 25),
        ("Barbarian", 25, 12, 10, 5),
        ("Cleric", 15, 10, 12, 18),
        ("Paladin", 15, 25, 18, 8),
        ("Druid", 15, 8, 25, 20),
        ("Bard", 5, 8, 25, 15)
    ]
    
    for name, hp, atk, def_, mp in card_specs:
        for _ in range(3):  # 3 copies of each card
            deck.append(Card(name, hp, atk, def_, mp))
    
    return deck

##########################################[EXAMPLE USAGE]##########################################
if __name__ == "__main__":
    deck = create_deck()
    
    # Sample hand of 6 cards
    hand = deck[:6]  # For simplicity, take the first 6 cards from the deck

    print("Initial Hand:")
    for card in hand:
        print(card)

    # Play a Cleric card
    play_card(hand[2], hand)  # Assume index 2 is Cleric

    print("\nAfter playing Cleric:")
    for card in hand:
        print(card)

    # Play a Bard card
    play_card(hand[5], hand)  # Assume index 5 is Bard

    print("\nAfter playing Bard:")
    for card in hand:
        print(card)