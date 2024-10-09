# spells.py
class SpellCard:
    def __init__(self, name, description, cost, effect):
        self.name = name
        self.description = description
        self.cost = cost
        self.effect = effect

    def play(self):
        return f"{self.name} is played. Effect: {self.effect}"

# Example spell cards
fireball = SpellCard("Fireball", "Deals 3 damage to a target unit.", cost=2, effect="3 damage to a target unit")
healing = SpellCard("Healing", "Heals 5 HP to a friendly unit.", cost=2, effect="Heals 5 HP")
lightning_bolt = SpellCard("Lightning Bolt", "Deals 6 damage to a target unit.", cost=3,
                           effect="6 damage to a target unit")
shield = SpellCard("Shield", "Grants a unit +3 HP.", cost=1, effect="Grants a unit +3 HP")
blizzard = SpellCard("Blizzard", "Deals 2 damage to all enemy units.", cost=4, effect="2 damage to all enemy units")