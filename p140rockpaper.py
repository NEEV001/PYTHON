import random
from colorama import Fore, Style, init
init()
    
c=0
while True:
    choices="rock","paper","scissor"

    comp=random.choice(choices)

    user=input(Fore.CYAN+"✊ Choose rock, paper or scissor => "+Style.RESET_ALL)

    print(Fore.YELLOW+"🤖 Comp choose", comp, Style.RESET_ALL)

    if user==comp:
        print(Fore.BLUE+"🤝 It's a draw"+Style.RESET_ALL)

    elif user=="rock" and comp=="scissor" or user=="paper" and comp=="rock" or user=="scissor" and comp=="paper":
        print(Fore.GREEN+"🎉 User won"+Style.RESET_ALL)
        c=c+1

    else:
        print(Fore.RED+"💻 Computer win"+Style.RESET_ALL)

    play=input(Fore.MAGENTA+"🔄 Do you want to play again? (yes,no) => "+Style.RESET_ALL)
    
    if play=="no":
        print(Fore.CYAN+"🙏 Thanks for playing")
        print("🏆 Final score is", c, Style.RESET_ALL)
        break