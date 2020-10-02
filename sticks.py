wins1 = 0
wins2 = 0
onehand0 = 99
onehand1 = 99
onehand2 = [1,1,2,0]
onehand3 = [1,2,3,0]
onehand4 = [2,2,3,1,4,0]
onehand5 = [2,3,4,1]
onehand6 = [3,3,4,2]
onehand7 = 99
onehand8 = 99
onehandadd = [onehand0,onehand1,onehand2,onehand3,onehand4,onehand5,onehand6,onehand7,onehand8]
print("Welcome to Sticks!")
print("Tip: Use 'left' and 'right' to indicate which hand you are choosing")
print()
while True:
    hand1 = 1
    hand2 = 1
    hand3 = 1
    hand4 = 1
    print ("Player One has won", wins1, "times and Player Two has won", wins2, "times." )
    rematch = input("Play? ('Y' or 'N'): ")
    if rematch == ("Y"):
        while True:
            arehit = 1
            arehit1 = 1
            print("Player 1:")
            print("Left Hand", hand1,"     ","Right Hand", hand2,)
            print()
            print("Player 2:")
            print("Left Hand", hand3,"     ","Right Hand", hand4,)
            print()
            oneaddhands = hand1 + hand2
            print("Player 1 do you want to hit or split? (Type 'hit' or 'split')")
            action = input(":")
            if action == ("split"):
                arehit = 0
                onehands = onehandadd[oneaddhands]
                if (onehands[0] == 99):
                    print("You cannot split or combine, please specify which hand you want to hit with")
                    select1 = input(":")
                    arehit = 1
                else:
                    onehandlength = len(onehands)
                    print ("You have:", hand1, "and", hand2,)
                    print ()
                    print ("You can turn that into:")
                    if onehandlength == 4:
                        if onehands[0] == hand1:
                            print (onehands[2], "and", onehands[3])
                            print()
                            wish1 = input("Player 1, do you wish to do this? ('Y' or 'N'):")
                            if wish1 == ("Y"):
                                hand1 = onehands[2]
                                hand2 = onehands[3]
                            else:
                                print()
                                print("You arent spliting or combining, so please specify which hand you want to hit with")
                                select1 = input(":")
                                arehit = 1
                        else:
                            if onehands[0] == hand2:
                                print (onehands[2], "and", onehands[3])
                                print()
                                wish1 = input("Player 1, do you wish to do this? ('Y' or 'N'):")
                                if wish1 == ("Y"):
                                    hand1 = onehands[2]
                                    hand2 = onehands[3]
                                else:
                                    print()
                                    print("You arent spliting or combining, so please specify which hand you want to hit with")
                                    select1 = input(":")
                                    arehit = 1
                            else:
                                print (onehands[0], "and", onehands[1])
                                print()
                                wish1 = input("Player 1, do you wish to do this? ('Y' or 'N'):")
                                if wish1 == ("Y"):
                                    hand1 = onehands[0]
                                    hand2 = onehands[1]
                                else:
                                    print()
                                    print("You arent spliting or combining, so please specify which hand you want to hit with")
                                    select1 = input(":")
                                    arehit = 1
                    else:
                        if hand1 == 0:
                            print ("2 and 2  or  3 and 1")
                            print()
                            wish1 = input("Player 1, do you want the first or second? ('1' or '2' or 'N' if neither):")
                            if wish1 == ("1"):
                                hand1 = 2
                                hand2 = 2
                            else:
                                if wish1 == ("2"):
                                    hand1 = 3
                                    hand2 = 1
                                else:
                                    print()
                                    print("You arent spliting or combining, so please specify which hand you want to hit with")
                                    select1 = input(":")
                                    arehit = 1
                        else:
                            if hand1 == 4:
                                print ("2 and 2  or  3 and 1")
                                print()
                                wish1 = input("Player 1, do you want the first or second? ('1' or '2' or 'N' if neither):")
                                if wish1 == ("1"):
                                    hand1 = 2
                                    hand2 = 2
                                else:
                                    if wish1 == ("2"):
                                        hand1 = 3
                                        hand2 = 1
                                    else:
                                        print()
                                        print("You arent spliting or combining, so please specify which hand you want to hit with")
                                        select1 = input(":")
                                        arehit = 1
                            else:
                                if hand1 == 2:
                                    print ("0 and 4  or  3 and 1")
                                    print()
                                    wish1 = input("Player 1, do you want the first or second? ('1' or '2' or 'N' if neither):")
                                    if wish1 == ("1"):
                                        hand1 = 0
                                        hand2 = 4
                                    else:
                                        if wish1 == ("2"):
                                            hand1 = 3
                                            hand2 = 1
                                        else:
                                            print()
                                            print("You arent spliting or combining, so please specify which hand you want to hit with")
                                            select1 = input(":")
                                            arehit = 1
                                else:
                                    if hand1 == 3:
                                        print ("0 and 4  or  2 and 2")
                                        print()
                                        wish1 = input("Player 1, do you want the first or second? ('1' or '2' or 'N' if neither):")
                                        if wish1 == ("1"):
                                            hand1 = 0
                                            hand2 = 4
                                        else:
                                            if wish1 == ("2"):
                                                hand1 = 2
                                                hand2 = 2
                                            else:
                                                print()
                                                print("You arent spliting or combining, so please specify which hand you want to hit with")
                                                select1 = input(":")
                                                arehit = 1
                                    else:
                                        if hand1 == 1:
                                            print ("0 and 4  or  2 and 2")
                                            print()
                                            wish1 = input("Player 1, do you want the first or second? ('1' or '2' or 'N' if neither):")
                                            if wish1 == ("1"):
                                                hand1 = 0
                                                hand2 = 4
                                            else:
                                                if wish1 == ("2"):
                                                    hand1 = 2
                                                    hand2 = 2
                                                else:
                                                    print()
                                                    print("You arent spliting or combining, so please specify which hand you want to hit with")
                                                    select1 = input(":")
                                                    arehit = 1
            else:
                print("Which hand do you want to hit with?")
                select1 = input(":")
                if arehit == 1:                   
                    print("Player 1, which hand will you hit?")
                    select2 = input(":")
                    print()
                    if select1 == ("left"):
                        if hand1 == 0:
                            print()
                            print("Sorry you cant use this hand, i'll use the correct one for you")
                            print()
                            hand3 = hand2 + hand3
                        if select2 == ("left"):
                            if hand3 == 0:
                                print("Sorry you cant choose this hand, i'll use the correct one for you")
                                print()
                                hand4 = hand1 + hand4
                            else:
                                hand3 = hand1 + hand3
                        else:
                            if hand4 == 0:
                                print("Sorry you cant choose this hand, i'll use the correct one for you")
                                print()
                                hand3 = hand1 + hand3
                            else:
                                hand4 = hand1 + hand4
                    else:
                        if hand2 == 0:
                            print()
                            print("Sorry you cant use this hand, i'll use the correct one for you")
                            print()
                            hand3 = hand1 + hand3
                        if select2 == ("left"):
                            if hand3 == 0:
                                print("Sorry you cant choose this hand, i'll use the correct one for you")
                                print()
                                hand4 = hand2 + hand4
                            else:
                                hand3 = hand2 + hand3
                        else:
                            if hand4 == 0:
                                print("Sorry you cant choose this hand, i'll use the correct one for you")
                                print()
                                hand3 = hand2 + hand3
                            else:
                                hand4 = hand2 + hand4
                    if (hand3 >= 5):
                        hand3 = hand3 - 5
                    if (hand4 >= 5):
                        hand4 = hand4 - 5
                    if hand3 == 0:
                        if hand4 == 0:
                            print()
                            print("Player 1 has won!")
                            wins1 = wins1 + 1
                            break
            print()
            print("Player 1:")
            print("Left Hand", hand1,"     ","Right Hand", hand2,)
            print()
            print("Player 2:")
            print("Left Hand", hand3,"     ","Right Hand", hand4,)
            print()
            oneaddhands = hand3 + hand4
            print("Player 2 do you want to hit or split? (Type 'hit' or 'split')")
            action2 = input(":")
            if action2 == ("split"):
                arehit1 = 0
                onehands = onehandadd[oneaddhands]
                if (onehands[0] == 99):
                    print("You cannot split or combine, please specify which hand you want to hit with")
                    select1 = input(":")
                    arehit1 = 1
                else:
                    onehandlength = len(onehands)
                    print ("You have:", hand3, "and", hand4)
                    print ()
                    print ("You can turn that into:")
                    if onehandlength == 4:
                        if onehands[0] == hand3:
                            print (onehands[2], "and", onehands[3])
                            print()
                            wish1 = input("Player 2, do you wish to do this? ('Y' or 'N'):")
                            if wish1 == ("Y"):
                                hand3 = onehands[2]
                                hand4 = onehands[3]
                            else:
                                print()
                                print("You arent spliting or combining, so please specify which hand you want to hit with")
                                select1 = input(":")
                                arehit1 = 1
                        else:
                            if onehands[0] == hand4:
                                print (onehands[2], "and", onehands[3])
                                print()
                                wish1 = input("Player 2, do you wish to do this? ('Y' or 'N'):")
                                if wish1 == ("Y"):
                                    hand3 = onehands[2]
                                    hand4 = onehands[3]
                                else:
                                    print()
                                    print("You arent spliting or combining, so please specify which hand you want to hit with")
                                    select1 = input(":")
                                    arehit1 = 1
                            else:
                                print (onehands[0], "and", onehands[1])
                                print()
                                wish1 = input("Player 2, do you wish to do this? ('Y' or 'N'):")
                                if wish1 == ("Y"):
                                    hand3 = onehands[0]
                                    hand4 = onehands[1]
                                else:
                                    print()
                                    print("You arent spliting or combining, so please specify which hand you want to hit with")
                                    select1 = input(":")
                                    arehit1 = 1
                    else:
                        if hand3 == 0:
                            print ("2 and 2  or  3 and 1")
                            print()
                            wish1 = input("Player 2, do you want the first or second? ('1' or '2' or 'N' if neither):")
                            if wish1 == ("1"):
                                hand3 = 2
                                hand4 = 2
                            else:
                                if wish1 == ("2"):
                                    hand3 = 3
                                    hand4 = 1
                                else:
                                    print()
                                    print("You arent spliting or combining, so please specify which hand you want to hit with")
                                    select1 = input(":")
                                    arehit1 = 1
                        else:
                            if hand3 == 4:
                                print ("2 and 2  or  3 and 1")
                                print()
                                wish1 = input("Player 2, do you want the first or second? ('1' or '2' or 'N' if neither):")
                                if wish1 == ("1"):
                                    hand3 = 2
                                    hand4 = 2
                                else:
                                    if wish1 == ("2"):
                                        hand3 = 3
                                        hand4 = 1
                                    else:
                                        print()
                                        print("You arent spliting or combining, so please specify which hand you want to hit with")
                                        select1 = input(":")
                                        arehit1 = 1
                            else:
                                if hand3 == 2:
                                    print ("0 and 4  or  3 and 1")
                                    print()
                                    wish1 = input("Player 2, do you want the first or second? ('1' or '2' or 'N' if neither):")
                                    if wish1 == ("1"):
                                        hand3 = 0
                                        hand4 = 4
                                    else:
                                        if wish1 == ("2"):
                                            hand3 = 3
                                            hand4 = 1
                                        else:
                                            print()
                                            print("You arent spliting or combining, so please specify which hand you want to hit with")
                                            select1 = input(":")
                                            arehit1 = 1
                                else:
                                    if hand3 == 3:
                                        print ("0 and 4  or  2 and 2")
                                        print()
                                        wish1 = input("Player 2, do you want the first or second? ('1' or '2' or 'N' if neither):")
                                        if wish1 == ("1"):
                                            hand3 = 0
                                            hand4 = 4
                                        else:
                                            if wish1 == ("2"):
                                                hand3 = 2
                                                hand4 = 2
                                            else:
                                                print()
                                                print("You arent spliting or combining, so please specify which hand you want to hit with")
                                                select1 = input(":")
                                                arehit1 = 1
                                    else:
                                        if hand3 == 1:
                                            print ("0 and 4  or  2 and 2")
                                            print()
                                            wish1 = input("Player 2, do you want the first or second? ('1' or '2' or 'N' if neither):")
                                            if wish1 == ("1"):
                                                hand3 = 0
                                                hand4 = 4
                                            else:
                                                if wish1 == ("2"):
                                                    hand3 = 2
                                                    hand4 = 2
                                                else:
                                                    print()
                                                    print("You arent spliting or combining, so please specify which hand you want to hit with")
                                                    select1 = input(":")
                                                    arehit1 = 1
            else:
                print("Which hand do you want to hit with?")
                select1 = input(":")
                if arehit1 == 1:
                    print("Player 2, which hand will you hit?")
                    select2 = input(":")
                    print()
                    if select1 == ("left"):
                        if hand3 == 0:
                            print()
                            print("Sorry you cant use this hand, i'll use the correct one for you")
                            print()
                            hand1 = hand4 + hand1
                        if select2 == ("left"):
                            if hand1 == 0:
                                print("Sorry you cant choose this hand, i'll use the correct one for you")
                                print()
                                hand2 = hand3 + hand2
                            else:
                                hand1 = hand3 + hand1
                        else:
                            if hand2 == 0:
                                print("Sorry you cant choose this hand, i'll use the correct one for you")
                                print()
                                hand1 = hand3 + hand1
                            else:
                                hand2 = hand3 + hand2
                    else:
                        if hand4 == 0:
                            print()
                            print("Sorry you cant use this hand, i'll use the correct one for you")
                            print()
                            hand1 = hand3 + hand1
                        if select2 == ("left"):
                            if hand1 == 0:
                                print("Sorry you cant choose this hand, i'll use the correct one for you")
                                print()
                                hand2 = hand4 + hand2
                            else:
                                hand1 = hand4 + hand1
                        else:
                            if hand2 == 0:
                                print("Sorry you cant choose this hand, i'll use the correct one for you")
                                print()
                                hand1 = hand4 + hand1
                            else:
                                hand2 = hand4 + hand2
            if (hand1 >= 5):
                hand1 = hand1 - 5
            if (hand2 >= 5):
                hand2 = hand2 - 5
            if hand3 == 0:
                if hand4 == 0:
                    print()
                    print("Player 2 has won!")
                    wins2 = wins2 + 1
                    break
    else:
        if (wins1 > wins2):
            print("Player 1 wins:", wins1, "to", wins2)
            break
        if (wins1 < wins2):
            print("Player 2 wins:", wins2, "to", wins1)
            break
        if (wins1 == wins2):
            print("It's a TIE! BOth players had", wins1, "wins. GG")
            break