def legit(word, letters):
    word = list(word)
    letters = list(letters)
    
    for letter in word:
        if letter not in letters:
            return False
        else:
            letters.remove(letter)
    
    return True

def score(word):
    points = {
    'e': 1, 'a': 1, 'i': 1, 'o': 1, 'n': 1,
    'r': 1, 't': 1, 'l': 1, 's': 1, 'u': 1,
    'd': 2, 'g': 2, 'b': 3, 'c': 3, 'm': 3,
    'p': 3, 'f': 4, 'h': 4, 'v': 4, 'w': 4,
    'y': 4, 'k': 5, 'j': 8, 'x': 8, 'q': 10,
    'z': 10 }
    
    return sum([points[letter] for letter in word])


w = [input() for i in range(int(input()))]  # available words
l = input()                                 # letters

candidates = [(word, score(word)) for word in w if legit(word, l)]

print(sorted(candidates, key = lambda t: t[1], reverse=True)[0][0])
