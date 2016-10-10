import random
player = random.randint(1, 6)
import random
computer = random.randint(1, 6)

print("You rolled a", player)
print("Computer rolled a", computer)

if player > computer:
    print("Winner is you.")
if player < computer:
    print("Winner is computer.")
