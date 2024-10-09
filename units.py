# units.py
class Card:
    def __init__(self, name, description, cost):
        self.name = name
        self.description = description
        self.cost = cost

class UnitCard(Card):
    def __init__(self, name, description, cost, attack, hp):
        super().__init__(name, description, cost)
        self.attack = attack
        self.hp = hp

    def play(self):
        return f"{self.name} is played with {self.attack} attack and {self.hp} HP."

# Example unit cards
barbarian = UnitCard("Barbarian", "Strong warrior", 2, 2, 10)
elf = UnitCard("Elf", "Swift archer", 1, 5, 6)
goblin = UnitCard("Goblin", "Sneaky attacker", 1, 4, 3)
dragon = UnitCard("Dragon", "Fire-breathing", 5, 7, 15)
knight = UnitCard("Knight", "Strong armor", 3, 6, 9)