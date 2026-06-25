list1 = ['__','__','__','__','__','__','__','__','__']
turn = 1

while turn < 10:


    if turn % 2 == 0:
        pos = int(input("enter ur pos player1=> "))
        if list1[pos-1]=='__':
           list1[pos-1] = 'X'
        else:
            print("already there")
            turn=turn-1

    else:
        pos = int(input("enter ur pos player2=> "))
        if list1[pos-1]=='__':
           list1[pos-1] = '0'
        else:
            print("already there")
            turn=turn-1
    
    print(list1[0], "|", list1[1], "|", list1[2])
    print(list1[3], "|", list1[4], "|", list1[5])
    print(list1[6], "|", list1[7], "|", list1[8])
    turn=turn+1

     

    if list1[0] == list1[1] == list1[2]:
        if list1[0] == '0':
            print("Player 2 wins")
            break
        elif list1[0] == 'X':
            print("Player 1 wins")
            break

    elif list1[3] == list1[4] == list1[5]:
        if list1[3] == '0':
            print("Player 2 wins")
            break
        elif list1[3] == 'X':
            print("Player 1 wins")
            break

    elif list1[6] == list1[7] == list1[8]:
        if list1[6] == '0':
            print("Player 2 wins")
            break
        elif list1[6] == 'X':
            print("Player 1 wins")
            break

    elif list1[0] == list1[3] == list1[6]:
        if list1[0] == '0':
            print("Player 2 wins")
            break
        elif list1[0] == 'X':
            print("Player 1 wins")
            break

    elif list1[1] == list1[4] == list1[7]:
        if list1[1] == '0':
            print("Player 2 wins")
            break
        elif list1[1] == 'X':
            print("Player 1 wins")
            break

    elif list1[2] == list1[5] == list1[8]:
        if list1[2] == '0':
            print("Player 2 wins")
            break
        elif list1[2] == 'X':
            print("Player 1 wins")
            break

    elif list1[0] == list1[4] == list1[8]:
        if list1[0] == '0':
            print("Player 2 wins")
            break
        elif list1[0] == 'X':
            print("Player 1 wins")
            break

    elif list1[2] == list1[4] == list1[6]:
        if list1[2] == '0':
            print("Player 2 wins")
            break
        elif list1[2] == 'X':
            print("Player 1 wins")
            break

    if turn == 10:
        print("Match Draw")