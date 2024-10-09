import tkinter as tk
from tkinter import messagebox
from units import UnitCard
import spells
import random

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

    def shuffle(self):
        cards = []
        current = self.head
        while current:
            cards.append(current.data)
            current = current.next
        random.shuffle(cards)

        # Rebuild the linked list with shuffled cards
        self.head = None
        for card in cards:
            self.append(card)

# Player Class
from units import barbarian, elf, goblin, dragon, knight
from spells import fireball, healing, lightning_bolt, blizzard

# Combined list of units and spells
all_cards = [barbarian, elf, goblin, dragon, knight, fireball, healing, lightning_bolt, blizzard]

# Player Class
class Player:
    def __init__(self, name, deck, hp=30):
        self.name = name
        self.deck = deck
        self.hand = []
        self.hp = hp
        self.played_units = []

        # Flags for turn actions
        self.card_played = False
        self.attacked = False

        # Draw 3 cards from the player's deck at the start of the game
        self.draw_initial_hand()

    def draw_initial_hand(self):
        # Draw 3 random cards from the combined list of units and spells
        for _ in range(3):
            card = random.choice(all_cards)
            self.hand.append(card)

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
                self.card_played = True  # Set flag when a card is played
                return card.play()
            elif card.name == "Healing":
                self.hp += 5  # Heal for 5 HP
                return f"{self.name} heals for 5 HP."
            elif card.name == "Fireball":
                return "Fireball spell cast!"
        else:
            return f"{self.name} has no card at index {index}."

    def attack(self, target_player):
        if self.attacked:
            return f"{self.name} has already attacked this turn."
        total_attack = sum(unit.attack for unit in self.played_units)
        target_player.hp -= total_attack
        self.attacked = True  # Set flag when an attack is made
        return f"{self.name} attacks {target_player.name} for {total_attack} damage!"

    def reset_turn_flags(self):
        self.card_played = False
        self.attacked = False

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

        self.play_card_buttons = []  # Store buttons for playing cards

        self.attack_button = tk.Button(self.root, text="Attack", command=self.attack)
        self.attack_button.pack()

        self.next_turn_button = tk.Button(self.root, text="End Turn", command=self.end_turn)
        self.next_turn_button.pack()

        # Game log display
        self.log_text = tk.Text(self.root, height=10, width=50)
        self.log_text.pack(side=tk.LEFT)
        self.log_text.insert(tk.END, "Game started.\n")

        # Player 1 and Player 2 draw their initial hands
        self.start_game()

        self.update_gui()

        # Start the GUI main loop
        self.root.mainloop()

    def start_game(self):
        # Both players draw their initial 3 cards
        action1 = self.player1.draw_card()
        action2 = self.player2.draw_card()
        self.log_action(action1)
        self.log_action(action2)
        self.update_gui()

    def update_gui(self):
        self.player1_label.config(text=f"{self.player1.name} HP: {self.player1.hp}")
        self.player2_label.config(text=f"{self.player2.name} HP: {self.player2.hp}")
        self.turn_label.config(text=f"Turn {self.turn}: {self.current_player.name}'s turn")

        hand_text = "Your hand:\n" + "\n".join([f"{i + 1}. {card.name}" for i, card in enumerate(self.current_player.hand)])
        self.hand_label.config(text=hand_text)

        # Clear previous play card buttons
        for button in self.play_card_buttons:
            button.destroy()
        self.play_card_buttons.clear()

        # Create a button for each card in hand
        for i, card in enumerate(self.current_player.hand):
            button = tk.Button(self.root, text=f"Play {card.name}", command=lambda index=i: self.play_card(index))
            button.pack()
            self.play_card_buttons.append(button)

    def log_action(self, message):
        self.log_text.insert(tk.END, message + '\n')
        self.log_text.see(tk.END)

    def play_card(self, index):
        action = self.current_player.play_card(index)
        self.log_action(action)
        self.update_gui()

        if action == "Fireball spell cast!":
            damage = 10  # Direct damage from Fireball
            self.opponent.hp -= damage
            self.log_action(f"{self.current_player.name} casts Fireball for {damage} damage!")
            if self.opponent.hp <= 0:
                self.log_action(f"{self.current_player.name} wins the game!")
                messagebox.showinfo("Game Over", f"{self.current_player.name} wins the game!")
                self.root.quit()
            self.update_gui()

    def attack(self):
        if not self.current_player.card_played:
            messagebox.showinfo("Action Not Allowed", "You must play a card before attacking.")
            return

        if self.current_player.played_units:
            damage = self.current_player.attack(self.opponent)
            self.log_action(damage)
            if self.opponent.hp <= 0:
                self.log_action(f"{self.current_player.name} wins the game!")
                messagebox.showinfo("Game Over", f"{self.current_player.name} wins the game!")
                self.root.quit()
            self.update_gui()
        else:
            messagebox.showinfo("No Units", "You have no units to attack with.")

    def end_turn(self):
        # Reset flags for the next turn
        self.current_player.reset_turn_flags()
        
        # Draw a new card at the start of the turn
        action = self.current_player.draw_card()
        self.log_action(action)

        # Switch players
        self.current_player, self.opponent = self.opponent, self.current_player
        self.turn += 1
        self.update_gui()

# Set up basic decks
deck1 = LinkedList()
deck2 = LinkedList()

# Import units and spells
from units import barbarian, elf, goblin, dragon, knight
from spells import fireball, healing, lightning_bolt, blizzard

# Add Unit and Spell Cards to decks
deck1.append(barbarian)
deck1.append(elf)
deck1.append(healing)  # Assume healing is a card
deck1.append(fireball)  # Assume fireball is a card

deck2.append(elf)
deck2.append(healing)  # Assume healing is a card
deck2.append(barbarian)

# Shuffle decks (optional, can be removed if decks should remain in order)
deck1.shuffle()
deck2.shuffle()

# Create players
player1 = Player("Player 1", deck1)
player2 = Player("Player 2", deck2)

# Start the game
game_gui = GameGUI(player1, player2)
