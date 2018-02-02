class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value
    
    def value(s):
        if s is "A": return 14
        elif s is "K": return 13
        elif s is "Q": return 12
        elif s is "J": return 11
        else: return int(s)
    
    def color(s):
        if s is "D": return 1
        elif s is "C": return 2
        elif s is "H": return 3
        else: return 4
    
    def create(s):
        if len(s) is 2:
            value = s[0]
            color = s[1]
        else:
            value = s[0:2]
            color = s[2]
        
        return Card(Card.color(color), Card.value(value))

def turn(deck1, deck2, towin1, towin2):
    card1 = deck1.pop(0)
    card2 = deck2.pop(0)

    towin1.append(card1)
    towin2.append(card2)

    if card1.value > card2.value:
        deck1 += towin1 + towin2
    elif card2.value > card1.value:
        deck2 += towin1 + towin2
    else:
        if len(deck1) >= 3 and len(deck2) >= 3:
            towin1 += deck1[:3]
            towin2 += deck2[:3]
            
            deck1.pop(0); deck2.pop(0)
            deck1.pop(0); deck2.pop(0)
            deck1.pop(0); deck2.pop(0)
            
            return turn(deck1, deck2, towin1, towin2)
        else:
            print("PAT")
            return True
    
    return False


deck1 = [Card.create(input()) for i in range(int(input()))]
deck2 = [Card.create(input()) for i in range(int(input()))]

n = 0
e = False

while not e:
    if not deck1:
        print("2 {}".format(n))
        e = True
    elif not deck2:
        print("1 {}".format(n))
        e = True
    else:
        e = turn(deck1, deck2, [], [])
        n += 1
