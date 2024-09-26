import tkinter as tk
from tkinter import messagebox

# Basic Card Classes
class Card:
    def __init__(self, name, description, cost):
        self.name = name
        self.description = description
        self.cost = cost

    def play(self):
        pass  # Placeholder method


class UnitCard(Card):
    def __init__(self, name, description, cost, attack, hp):
        super().__init__(name, description, cost)
        self.attack = attack
        self.hp = hp

    def play(self):
        return f"{self.name} is played with {self.attack} attack and {self.hp} HP."


class SpellCard(Card):
    def __init__(self, name, description, cost, effect):
        super().__init__(name, description, cost)
        self.effect = effect

    def play(self):
        return f"{self.name} is played. Effect: {self.effect}"


# Linked List for Deck
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, card):
        new_node = Node(card)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def draw(self):
        if not self.head:
            return None
        drawn_card = self.head.data
        self.head = self.head.next
        return drawn_card


# Player Class
class Player:
    def __init__(self, name, deck, hp=30):
        self.name = name
        self.deck = deck
        self.hand = []
        self.hp = hp
        self.played_units = []

    def draw_card(self):
        card = self.deck.draw()
        if card:
            self.hand.append(card)
            return f"{self.name} draws {card.name}"
        else:
            return f"{self.name} has no more cards to draw."

    def play_card(self, index):
        if index < len(self.hand):
            card = self.hand.pop(index)
            if isinstance(card, UnitCard):
                self.played_units.append(card)
            return card.play()
        else:
            return f"{self.name} has no card at index {index}."

    def attack(self, target_player):
        total_attack = sum(unit.attack for unit in self.played_units)
        target_player.hp -= total_attack
        return f"{self.name} attacks {target_player.name} for {total_attack} damage!"


# Game Class with GUI
class GameGUI:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.opponent = player2
        self.turn = 1

        # Create the main window
        self.root = tk.Tk()
        self.root.title("Homebrew Card Game")

        # Labels and Buttons for the GUI
        self.turn_label = tk.Label(self.root, text=f"Turn {self.turn}: {self.current_player.name}'s turn", font=("Arial", 14))
        self.turn_label.pack()

        self.player1_label = tk.Label(self.root, text=f"{player1.name} HP: {player1.hp}")
        self.player1_label.pack()

        self.player2_label = tk.Label(self.root, text=f"{player2.name} HP: {player2.hp}")
        self.player2_label.pack()

        self.hand_label = tk.Label(self.root, text="Your hand:")
        self.hand_label.pack()

        self.play_card_button = tk.Button(self.root, text="Play Card", command=self.play_card)
        self.play_card_button.pack()

        self.attack_button = tk.Button(self.root, text="Attack", command=self.attack)
        self.attack_button.pack()

        self.next_turn_button = tk.Button(self.root, text="End Turn", command=self.end_turn)
        self.next_turn_button.pack()

        # Game log display
        self.log_text = tk.Text(self.root, height=10, width=50)
        self.log_text.pack(side=tk.LEFT)
        self.log_text.insert(tk.END, "Game started.\n")

        self.update_gui()

        # Start the GUI main loop
        self.root.mainloop()

    def update_gui(self):
        # Update labels for player HP, turn, and hand
        self.player1_label.config(text=f"{self.player1.name} HP: {self.player1.hp}")
        self.player2_label.config(text=f"{self.player2.name} HP: {self.player2.hp}")
        self.turn_label.config(text=f"Turn {self.turn}: {self.current_player.name}'s turn")

        hand_text = "Your hand:\n" + "\n".join([f"{i+1}. {card.name}" for i, card in enumerate(self.current_player.hand)])
        self.hand_label.config(text=hand_text)

    def log_action(self, message):
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)

    def play_card(self):
        if self.current_player.hand:
            action = self.current_player.play_card(0)  # Play the first card in hand
            self.log_action(action)
            self.update_gui()
        else:
            messagebox.showinfo("No Cards", "You have no cards to play.")

    def attack(self):
        if self.current_player.played_units:
            damage = self.current_player.attack(self.opponent)
            self.log_action(damage)
            if self.opponent.hp <= 0:
                self.log_action(f"{self.current_player.name} wins the game!")
                messagebox.showinfo("Game Over", f"{self.current_player.name} wins the game!")
                self.root.quit()  # End the game
            self.update_gui()
        else:
            messagebox.showinfo("No Units", "You have no units to attack with.")

    def end_turn(self):
        # Switch the current player
        self.current_player, self.opponent = self.opponent, self.current_player
        self.turn += 1

        # Force the current player to draw a card
        action = self.current_player.draw_card()
        self.log_action(action)

        self.update_gui()


# Set up basic decks with placeholder cards
deck1 = LinkedList()
deck2 = LinkedList()

for i in range(5):
    deck1.append(UnitCard(f"Unit {i+1}", "A placeholder unit card", cost=1, attack=i+1, hp=i+2))
    deck2.append(UnitCard(f"Unit {i+6}", "A placeholder unit card", cost=1, attack=i+2, hp=i+3))

# Create players
player1 = Player("Player 1", deck1)
player2 = Player("Player 2", deck2)

# Start the game with a GUI
game_gui = GameGUI(player1, player2)
