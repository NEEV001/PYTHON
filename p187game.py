import os
from colorama import Fore, init

init(autoreset=True)

# 1-9 placeholders make it easy for players to map inputs to the real board grid
list1 = [' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 ']
turn = 1

def print_board():
    # Clears the terminal screen depending on OS to keep the layout static
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(Fore.CYAN + "┌───────────┐")
    
    # Row 1
    r1_col1 = Fore.BLUE + list1[0] if 'X' in list1[0] else Fore.RED + list1[0] if '0' in list1[0] else Fore.LIGHTBLACK_EX + list1[0]
    r1_col2 = Fore.BLUE + list1[1] if 'X' in list1[1] else Fore.RED + list1[1] if '0' in list1[1] else Fore.LIGHTBLACK_EX + list1[1]
    r1_col3 = Fore.BLUE + list1[2] if 'X' in list1[2] else Fore.RED + list1[2] if '0' in list1[2] else Fore.LIGHTBLACK_EX + list1[2]
    print(f"│{r1_col1}│{r1_col2}│{r1_col3}│")
    print(Fore.CYAN + "├───┼───┼───┤")
    
    # Row 2
    r2_col1 = Fore.BLUE + list1[3] if 'X' in list1[3] else Fore.RED + list1[3] if '0' in list1[3] else Fore.LIGHTBLACK_EX + list1[3]
    r2_col2 = Fore.BLUE + list1[4] if 'X' in list1[4] else Fore.RED + list1[4] if '0' in list1[4] else Fore.LIGHTBLACK_EX + list1[4]
    r2_col3 = Fore.BLUE + list1[5] if 'X' in list1[5] else Fore.RED + list1[5] if '0' in list1[5] else Fore.LIGHTBLACK_EX + list1[5]
    print(f"│{r2_col1}│{r2_col2}│{r2_col3}│")
    print(Fore.CYAN + "├───┼───┼───┤")
    
    # Row 3
    r3_col1 = Fore.BLUE + list1[6] if 'X' in list1[6] else Fore.RED + list1[6] if '0' in list1[6] else Fore.LIGHTBLACK_EX + list1[6]
    r3_col2 = Fore.BLUE + list1[7] if 'X' in list1[7] else Fore.RED + list1[7] if '0' in list1[7] else Fore.LIGHTBLACK_EX + list1[7]
    r3_col3 = Fore.BLUE + list1[8] if 'X' in list1[8] else Fore.RED + list1[8] if '0' in list1[8] else Fore.LIGHTBLACK_EX + list1[8]
    print(f"│{r3_col1}│{r3_col2}│{r3_col3}│")
    
    print(Fore.CYAN + "└───────────┘")

while turn < 10:
    print_board()

    if turn % 2 == 0:
        pos = int(input(Fore.BLUE + "❌ Player 1 (X) => Enter position: "))
        if 'X' not in list1[pos-1] and '0' not in list1[pos-1]:
            list1[pos-1] = ' X '
        else:
            input(Fore.YELLOW + "⚠️ Position already occupied! Press Enter to retry...")
            continue
    else:
        pos = int(input(Fore.RED + "⭕ Player 2 (0) => Enter position: "))
        if 'X' not in list1[pos-1] and '0' not in list1[pos-1]:
            list1[pos-1] = ' 0 '
        else:
            input(Fore.YELLOW + "⚠️ Position already occupied! Press Enter to retry...")
            continue  
    
    # Check winning conditions
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Columns
        (0, 4, 8), (2, 4, 6)             # Diagonals
    ]
    
    game_won = False
    for a, b, c in win_conditions:
        if list1[a] == list1[b] == list1[c]:
            print_board()
            if 'X' in list1[a]:
                print(Fore.GREEN + "🎉🏆 Player 1 (X) wins! 🏆🎉")
            else:
                print(Fore.GREEN + "🎉🏆 Player 2 (0) wins! 🏆🎉")
            game_won = True
            break
            
    if game_won:
        break

    turn += 1

if turn == 10 and not game_won:
    print_board()
    print(Fore.MAGENTA + "🤝 It's a Draw! Game Over. 🤝")