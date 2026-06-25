import random

# Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

board={
    4:14,
    9:31,
    17:7,
    20:38,
    28:84,
    40:59,
    51:67,
    54:34,
    62:19,
    64:60,
    63:81,
    87:24,
    93:73,
    95:75,
    99:78
}

print(MAGENTA + "="*50)
print("🐍🪜 WELCOME TO SNAKES & LADDERS 🪜🐍")
print("="*50 + RESET)

pos1=0
pos2=0

while pos1<100 and pos2<100:

    input(CYAN + "\n🎮 Player 1 press ENTER for dice => " + RESET)

    dice=random.randint(1,6)
    print(YELLOW + f"🎲 Dice = {dice}" + RESET)

    if pos1+dice<=100:
        pos1=pos1+dice

    print(BLUE + f"🚶 Player 1 reached {pos1}" + RESET)

    if pos1 in board:
        new_pos=board[pos1]

        if new_pos>pos1:
            print(GREEN + f"🪜 Ladder! Climb to {new_pos}" + RESET)
        else:
            print(RED + f"🐍 Snake! Slide to {new_pos}" + RESET)

        pos1=new_pos

    print(BLUE + f"📍 Current Position: {pos1}" + RESET)

    if pos1==100:
        print(GREEN + "\n🏆🎉 PLAYER 1 WINS 🎉🏆" + RESET)
        break

    input(CYAN + "\n🎮 Player 2 press ENTER for dice => " + RESET)

    dice=random.randint(1,6)
    print(YELLOW + f"🎲 Dice = {dice}" + RESET)

    if pos2+dice<=100:
        pos2=pos2+dice

    print(MAGENTA + f"🚶 Player 2 reached {pos2}" + RESET)

    if pos2 in board:
        new_pos=board[pos2]

        if new_pos>pos2:
            print(GREEN + f"🪜 Ladder! Climb to {new_pos}" + RESET)
        else:
            print(RED + f"🐍 Snake! Slide to {new_pos}" + RESET)

        pos2=new_pos

    print(MAGENTA + f"📍 Current Position: {pos2}" + RESET)

    if pos2==100:
        print(GREEN + "\n🏆🎉 PLAYER 2 WINS 🎉🏆" + RESET)
        break

print(MAGENTA + "\n🎯 GAME OVER 🎯" + RESET)