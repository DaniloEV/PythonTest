import sys
import random
from enum import Enum

# Enum que permite guardar los valores
class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("")
# El input es string
playerchoice = input(
    "Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

player = int(playerchoice)
# cambió el | con el or
# esto es porque
if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3.")
# El random es string (por extraño que parezca)
computerchoice = random.choice("123")

computer = int(computerchoice)

print("")

## antes con el replace print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
## antes con el replace print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".") 
# Choose (present) and chose (past) are different tenses of the same verb
print("You chose " + str(RPS(player).name.capitalize()) + ".")
print("Python chose " + str(RPS(computer).name.capitalize()) + ".")
print("")

if player == 1 and computer == 3:
    print("🎉 You win!")
elif player == 2 and computer == 1:
    print("🎉 You win!")
elif player == 3 and computer == 2:
    print("🎉 You win!")
elif player == computer:
    print("😲 Tie game!")
else:
    print("🐍 Python wins!")