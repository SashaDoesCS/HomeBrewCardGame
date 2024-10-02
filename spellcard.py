class Card:
    def __init__(self, name, description, cost):
        self.name = name
        self.description = description
        self.cost = cost

    def play(self):
        pass

class SpellCard(Card):
    def __init__(self, name, description, cost, effect):
        super().__init__(name, description, cost)
        self.effect = effect

    def play(self):
        print(f"{self.name} is played. Description: {self.description}, Cost: {self.cost} MP. Effect: {self.effect}")

class HealCard(SpellCard):
    def __init__(self, name, description, effect, cost, hp_amount):
        super().__init__(name, cost, description, effect)
        self.hp_amount = hp_amount

    def play(self, unit):
        return f"{self.name} restores {self.heal_amount} HP."

class StrengthCard(SpellCard):
    def __init__(self, name, description, effect, cost, atk_amount):
        super().__init__(name, cost, description, effect)
        self.atk_amount = atk_amount

    def play(self, unit):
        return f"{self.name} enhances ATK by {self.atk_amount}."

class DefenseCard(SpellCard):
    def __init__(self, name, description, effect, cost, def_amount):
        super().__init__(name, cost, description, effect)
        self.def_amount = def_amount

    def play(self, unit):
        return f"{self.name} enhances DEF by {self.def_amount}."

class ManaCard(SpellCard):
    def __init__(self, name, description, effect, cost, mp_amount):
        super().__init__(name, cost, description, effect)
        self.mp_amount = mp_amount

    def play(self):
        return f"{self.name} restores {self.mp_amount} MP."

class DirectCard(SpellCard):
    def __init__(self, name, description, effect, cost, dmg_amount):
        super().__init__(name, cost, description, effect)
        self.dmg_amount = dmg_amount

    def play(self, unit):
        return f"{self.name} deals {self.dmg_amount} to the enemy."

class ReduceATKCard(SpellCard):
    def __init__(self, name, description, effect, cost, reduce_atk_amount):
        super().__init__(name, cost, description, effect)
        self.reduce_atk_amount = reduce_atk_amount

    def play(self):
        return f"{self.name} reduces enemy attack by {self.reduce_atk_amount}."

class ReduceDEFCard(SpellCard):
    def __init__(self, name, description, effect, cost, reduce_def_amount):
        super().__init__(name, cost, description, effect)
        self.reduce_def_amount = reduce_def_amount

    def play(self, unit):
        return f"{self.name} reduces enemy attack by {self.reduce_def_amount}."

class LevelUpCard(SpellCard):
    def __init__(self, name, description, effect, cost, level_up):
        super().__init__(name, cost, description, effect)
        self.level_up = level_up

    #added this code to test with a premade unit class, feel free to delete
    def play(self, unit):
        for _ in range(self.level_up):
            unit.level_up()

    def __str__(self):
        return f"{self.name} has leveled up a unit."

class SightCard(SpellCard):
    def __init__(self, name, description, effect, cost, exp):
        super().__init__(name, cost, description, effect)

    def play(self):
        return f"{self.name} has revealed the opponent's deck."

class NullCard(SpellCard):
    def __init__(self, name, description, effect, cost, exp):
        super().__init__(name, cost, description, effect)

    def play(self):
        return f"{self.name} has removed a card from the opponent's deck."
