
from random import choice

def rockpaptercalculation():
    valid_moves = ["rock", "paper", "scissors"]
    computer = choice(valid_moves)

    player = input("Player, make your move: ").lower()

    if player not in valid_moves:
        print("Please enter a valid move!")
    elif player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
        (player == "paper" and computer == "rock") or \
        (player == "scissors" and computer == "paper"):
        print("Player wins!")
    else:
        print("Computer wins!")

    print(f"Computer plays {computer}")
rockpaptercalculation()

play=(input("You want to play again? Enter Yes or NO"))
if play=='yes'or 'no':
    rockpaptercalculation()
else :
    pass
    
