import random
names = [list("hogwarts"), list("python"), list("engineering"), list("electrical"), list("btech"), list("spell"), list("wand")]
word = random.choice(names)
guess=['_']*len(word)
chances = len(word)
b = False
while (chances > 0 and b == False):
    print("Chances left:",chances)
    print(' '.join(guess))
    x = input("Guess a letter: ")
    if x not in word:
        print("Wrong guess")
        chances -= 1
    else:
        if x not in guess:
            n = len(word)
            for i in range(n):
                if (word[i] == x):
                    guess[i] = x
            if '_' not in guess:
                b = True
        else:
            print("You re-entered same letter")
if '_' not in guess:
    print("Your guess is correct!")
    print("The word is",''.join(guess))
else:
    print("Failed")