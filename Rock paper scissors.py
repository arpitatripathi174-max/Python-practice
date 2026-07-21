import random

choices = ["rock", "paper", "scissors"]

# User choice
user = input("Enter rock, paper, or scissors: ").lower()

# Computer choice
computer = random.choice(choices)

print("You chose:", user)
print("Computer chose:", computer)

# Determine winner
if user == computer:
    print("It's a tie!")
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("You win!")
elif user in choices:
    print("Computer wins!")
else:
    print("Invalid choice! Please enter rock, paper, or scissors.")
