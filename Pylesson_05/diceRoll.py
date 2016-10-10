import random
player = random.randint(1, 6)
computer = random.randint(1, 6)

print("You rolled a", player)
print("Computer rolled a", computer)

def rollDice():
    global player, computer
    if player > computer:
        return "player"
    if player < computer:
        return "computer"
print("Winner is", rollDice())
