hands = [1,1]
hands_2 = [1,1]
def printhands():
    print("Player 1: "+str(hands))
    print("Player 2: "+str(hands_2))
def change(hands, hands_2, hitorsplit):
    if hitorsplit == "H":
        while True:
            which_hand = input("Which hand would you like to hit with? (1 or 2): ")
            which_hit = input("Which hand would you like to hit? (1 or 2): ")
            if not hands[int(which_hand)-1] == 0 and not hands_2[int(which_hit)-1] == 0:
                break
            else:
                print("Can't hit with this hand or can't hit this hand")
        hands_2[int(which_hit)-1] += hands[int(which_hand)-1]
        if hands_2[int(which_hit)-1] > 4:
            hands_2[int(which_hit) - 1] -= 5
    if hitorsplit == "S":
        options = []
        alt_hands = hands.copy()
        alt_hands.reverse()
        sum_1 = sum(hands)
        for i in range(int(sum_1/2)+1):
            current_hand = []
            current_hand.append(i)
            current_hand.append(sum_1-i)
            alt_current = current_hand.copy()
            alt_current.reverse()
            if not alt_hands == current_hand and not hands == current_hand and not alt_current in options and current_hand[0] < 5 and current_hand[1] < 5:
                options.append(current_hand)
        print("Your options are: ")
        for i in range(len(options)):
            print(str(i+1)+": "+str(options[i]))
        while True:
            choose = input("Which one do you want? (1-"+str(len(options))+"): ")
            if int(choose) <= len(options):
                hands = options[int(choose)-1]
                break
            else:
                print("Not a valid option")
    print("")
    return hands, hands_2
while True:
    printhands()
    while True:
        hitorsplit = input("Player 1: Hit or Split(H or S): ")
        if sum(hands) > 6 or sum(hands) < 2 and hitorsplit == "S":
            print("Can't Split")
        else:
            break
    thingies = change(hands, hands_2, hitorsplit)
    hands = thingies[0]
    hands_2 = thingies[1]
    if hands == [0,0] or hands_2 == [0,0]:
        print("Player 1 Wins!")
        break
    printhands()
    while True:
        hitorsplit = input("Player 2: Hit or Split(H or S): ")
        if sum(hands_2) > 6 or sum(hands_2) < 2 and hitorsplit == "S":
            print("Can't Split")
        else:
            break
    thingies = change(hands_2, hands, hitorsplit)
    hands = thingies[1]
    hands_2 = thingies[0]
    if hands == [0,0] or hands_2 == [0,0]:
        print("Player 2 Wins!")
        break
