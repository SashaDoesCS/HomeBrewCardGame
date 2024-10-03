##########################################[DEFINING CARD CLASS + EFFECTS]##########################################

class Card:
    def __init__(self, name, hp, atk, def_, mp):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.def_ = def_
        self.mp = mp
        self.is_disabled = False #Bard's doing

     #I added this status effect function to make effects to the stats easier to look at
    def status_effect(self, amount, effect_type):
        if effect_type == "heal":
            self.hp += amount
        elif effect_type == "atk":
            self.atk += amount
        elif effect_type == "def":
            self.def_ += amount
        elif effect_type == "mp":
            self.mp += amount
        elif effect_type == "reduce_atk":
            self.atk -= amount
            if self.atk < 0:
                self.atk = 0
        elif effect_type == "reduce_def":
            self.def_ -= amount
            if self.def_ < 0:
                self.def_ = 0

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

#Except for the status_effect function, everything above comes from Thomas' unit code, I put it here so I could test easier.

class BaseCard:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def play(self):
        pass

class SpellCard(BaseCard):
    def __init__(self, name, cost, effect):
        super().__init__(name, cost)
        self.effect = effect

    def __str__(self):
        return f"{self.name} is played. Cost: {self.cost} MP. Effect: {self.effect}"

class HealCard(SpellCard):
    def __init__(self, name, effect, cost, hp_amount):
        super().__init__(name, cost, effect)
        self.hp_amount = hp_amount

    def play(self, unit):
        print(f"{self.name} restores {self.hp_amount} HP on {unit.name}.")
        unit.status_effect(self.hp_amount, "heal")

class StrengthCard(SpellCard):
    def __init__(self, name, effect, cost, atk_amount):
        super().__init__(name, cost, effect)
        self.atk_amount = atk_amount

    def play(self, unit):
        print(f"{self.name} enhances ATK of {unit.name} by {self.atk_amount}.")
        unit.stauts_effect(self.atk_amount, "atk")

class DefenseCard(SpellCard):
    def __init__(self, name, effect, cost, def_amount):
        super().__init__(name, cost, effect)
        self.def_amount = def_amount

    def play(self, unit):
        print(f"{self.name} enhances DEF of {unit.name} by {self.def_amount}.")
        unit.status_effect(self.def_amount, "def")

class ManaCard(SpellCard):
    def __init__(self, name, effect, cost, mp_amount):
        super().__init__(name, cost, effect)
        self.mp_amount = mp_amount

    def play(self, unit):
        print(f"{self.name} restores {self.mp_amount} MP to {unit.name}.")
        unit.status_effect(self.mp_amount, "mp")

class ReduceATKCard(SpellCard):
    def __init__(self, name, effect, cost, reduce_atk_amount):
        super().__init__(name, cost, effect)
        self.reduce_atk_amount = reduce_atk_amount

    def play(self, unit):
        print(f"{self.name} reduces {unit.name}'s attack by {self.reduce_atk_amount}.")
        unit.status_effect(self.reduce_atk_amount, "reduce_atk")

class ReduceDEFCard(SpellCard):
    def __init__(self, name, effect, cost, reduce_def_amount):
        super().__init__(name, cost, effect)
        self.reduce_def_amount = reduce_def_amount

    def play(self, unit):
        print(f"{self.name} reduces {unit.name}'s defense by {self.reduce_def_amount}.")
        unit.status_effect(self.reduce_def_amount, "reduce_def")

class DirectCard(SpellCard):
    def __init__(self, name, effect, cost, dmg_amount):
        super().__init__(name, cost, effect)
        self.dmg_amount = dmg_amount

    def play(self, unit):
        return f"{self.name} deals {self.dmg_amount} to {unit.name}."

#Possibly delete Level Up Card since it seems unecessary?
class LevelUpCard(SpellCard):
    def __init__(self, name, effect, cost, level_up):
        super().__init__(name, cost, effect)
        self.level_up = level_up

    def play(self, unit):
        for _ in range(self.level_up):
            unit.level_up()
        print(f"{self.name} has leveled up {unit.name}.")

class SightCard(SpellCard):
    def __init__(self, name, effect, cost, exp):
        super().__init__(name, cost, effect)

    def play(self):
        print(f"{self.name} has revealed the opponent's deck.")

class NullCard(SpellCard):
    def __init__(self, name, effect, cost, exp):
        super().__init__(name, cost, effect)

    def play(self):
        print(f"{self.name} has removed a card from the opponent's deck.")
