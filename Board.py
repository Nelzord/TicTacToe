import time

def board():
    flag = False
    top = ["-", "-", "-"]
    mid = ["-", "-", "-"]
    bot = ["-", "-", "-"]
    while flag is False:
        time.sleep(.2)
        print(
            "Choices: Top Left, Top Middle, Top Right, Middle Left, Center, Middle Right, Bottom Left, Bottom Middle, Bottom Right")
        print "_____________________________________________________________________________________________________________________"
        move = raw_input("Player one, where do yo want to mark?")
        choice(move, "X", top, mid, bot)
        print
        printboard(top, mid, bot)
        print
        if validate(top, mid, bot, flag) is True:
            time.sleep(.2)
            print("Player one wins!")
            playagain = raw_input("Do you want to play again? (Yes/No)")
            print(playagain)
            if playagain is not "No":
                clearboard(), newgame()
            else:
                return
        move2 = raw_input("Player two, where do you want to mark?")
        choice(move2, "O", top, mid, bot)
        print
        printboard(top, mid, bot)
        print
        if validate(top, mid, bot, flag) is True:
            time.sleep(.2)
            print("Player two wins!")
            playagain = raw_input("Do you want to play again? (Yes/No)")
            if playagain is not "No":
                clearboard(), newgame()
            else:
                return

def validate(top, mid, bot, flag):
    directions = [top, mid, bot]
    for i in directions:
        if i[0] is not '-' and (i[0] is i[1] is i[2]):
            flag = True
            return flag
    for i in range(3):
        if top[i] is not '-' and (top[i] is mid[i] is bot[i]):
            flag = True
            return flag
    if top[0] is not '-' and top[0] is mid[1] is bot[2]:
        flag = True
        return flag
    if top[2] is not '-' and top[2] is mid[1] is bot[0]:
        flag = True
        return flag

def choice(mark, player, top, mid, bot):
    time.sleep(.2)
    if mark == "Top Left":
        if top[0] != '-':
            mark = raw_input("That spot is already taken, choose another.")
            choice(mark, player, top, mid, bot)
        else:
            top[0] = player
            return top
    elif mark == "Top Middle":
        if top[1] != '-':
            mark = raw_input("That spot is already taken, choose another.")
            choice(mark, player, top, mid, bot)
        else:
            top[1] = player
            return top
    elif mark == "Top Right":
        if top[2] != '-':
            mark = raw_input("That spot is already taken, choose another.")
            choice(mark, player, top, mid, bot)
        else:
            top[2] = player
            return top
    elif mark == "Middle Left":
        if mid[0] != '-':
            mark = raw_input("That spot is already taken, choose another.")
            choice(mark, player, top, mid, bot)
        else:
            mid[0] = player
            return mid
    elif mark == "Center":
        if mid[1] != '-':
            mark = raw_input("That spot is already taken, choose another.")
            choice(mark, player, top, mid, bot)
        else:
            mid[1] = player
            return mid
    elif mark == "Middle Right":
        if mid[2] != '-':
            mark = raw_input("That spot is already taken, choose another.")
            choice(mark, player, top, mid, bot)
        else:
            mid[2] = player
            return mid
    elif mark == "Bottom Left":
        if bot[0] != '-':
            mark = raw_input("That spot is already taken, choose another.")
            choice(mark, player, top, mid, bot)
        else:
            bot[0] = player
            return bot
    elif mark == "Bottom Middle":
        if bot[1] != '-':
            mark = raw_input("That spot is already taken, choose another.")
            choice(mark, player, top, mid, bot)
        else:
            bot[1] = player
            return bot
    elif mark == "Bottom Right":
        if bot[2] != '-':
            mark = raw_input("That spot is already taken, choose another.")
            choice(mark, player, top, mid, bot)
        else:
            bot[2] = player
            return bot
    else:
        mark = raw_input("That direction does not exist, please try again")
        choice(mark, player, top, mid, bot)

def opening():
    print "_____ _        _____            _____"
    time.sleep(.2)
    print "|_   _|_|___   |_   _|___ ___   |_   _|"
    time.sleep(.2)
    print "  | | | |  _|    | | | .'|  _|    | | | . | -_|"
    time.sleep(.2)
    print "  |_| |_|___|    |_| |__,|___|    |_| |___|___|"
    print

def clearboard():
    print "  ___________"
    time.sleep(.2)
    print "'._==_==_=_.'"
    time.sleep(.2)
    print " .-\:      /-."
    time.sleep(.2)
    print "| (|:.     |) |"
    time.sleep(.2)
    print '  -|:.     |-'
    time.sleep(.2)
    print "   \::.    / "
    time.sleep(.2)
    print "    '::. .'"
    time.sleep(.2)
    print "      ) ("
    time.sleep(.2)
    print "    _.' '._"
    time.sleep(.2)
    print "    """""""""
    time.sleep(.2)
    print " _ _ _ _ "
    time.sleep(.2)
    print " | | | |_|___ ___ ___ ___"
    time.sleep(.2)
    print " | | | | |   |   | -_|  _|"
    time.sleep(.2)
    print " |_____|_|_|_|_|_|___|_|"
    print
    print
    
def players():
    time.sleep(.2)
    print("Player one is X")
    print "_______________"
    time.sleep(.2)
    print("Player two is O")
    print "_______________"

def printboard(top, mid, bot):
    print("| " + top[0] + " | " + top[1] + " | " + top[2] + " |")
    print "+---+---+---+-"
    print("| " + mid[0] + " | " + mid[1] + " | " + mid[2] + " |")
    print "+---+---+---+-"
    print("| " + bot[0] + " | " + bot[1] + " | " + bot[2] + " |")

def newgame():
    players()
    board()

opening()
newgame()

