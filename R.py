from card import Card
import random

shuffled_deck = Card.new_deck()

class Player():
    def __init__(self, deck, hand, score):
        self.deck = deck
        self.hand = hand
        self.score = score

class Human(Player):
    def __init__(self, deck):
        super().__init__(deck, [], 0)
        first_half = deck[:len(deck) // 2]  # Get the first half of the deck
        self.hand = first_half[:6]  # Draw six cards from the first half

    def choose_card_from_hand(self):
        print("Your Hand:")
        for index, card in enumerate(self.hand, 1):
            print(f"{index}. {card}")

        while True:
            try:
                choice_index = int(input("Enter the number corresponding to your choice: ")) - 1
                if 0 <= choice_index < len(self.hand):
                    return self.hand.pop(choice_index)
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")


class Computer(Player):
    def __init__(self, deck):
        second_half = deck[len(deck) // 2:]  # Get the second half of the deck
        self.hand = second_half[:6]  # Draw six cards from the second half
        self.score = 0  # Initialize the score to zero

# Calculate the midpoint to split the list
midpoint = len(shuffled_deck) // 2

# Split the list into two halves
first_half = shuffled_deck[:midpoint]
second_half = shuffled_deck[midpoint:]

# Randomize the order of elements in each split
random.shuffle(first_half)
random.shuffle(second_half)

# Create instances of Human and Computer players
human_player = Human(first_half)
computer_player = Computer(second_half)

# Print the results
print("First Half (Randomized):", first_half)
print("Second Half (Randomized):", second_half)

# Player's turn
chosen_card = human_player.choose_card_from_hand()
print("You chose:", chosen_card)

# Computer's turn
# Find the highest card in the computer player's hand
highest_card = None
for card in computer_player.hand:
    if highest_card is None or card.value > highest_card.value:
        highest_card = card
print("Computer chose:", highest_card)

# ... (previous code remains unchanged) ...

# Player's turn
chosen_card = human_player.choose_card_from_hand()
print("You chose:", chosen_card)

# Computer's turn
computer_highest_card = max(computer_player.hand, key=lambda card: card.value)
print("Computer chose:", computer_highest_card)

# Compare the values of the chosen cards to determine the winner
if chosen_card.value > computer_highest_card.value:
    print("You win!")
elif chosen_card.value < computer_highest_card.value:
    print("Computer wins!")
else:
    print("It's a tie!")
