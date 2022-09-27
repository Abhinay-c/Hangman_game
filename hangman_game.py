word = ['h','o','g','w','a','r','t','s']
guess=['_','_','_','_','_','_','_','_']
chances = 12
b = False
while (chances > 0 and b == False):
    print("Your remaining chances are:",chances)
    print(''.join(guess))
    x = input("Guess a letter: ")
    if x not in word:
        print("Wrong guess")
        chances -= 1
    else:
        n = len(word)
        for i in range(n):
            if (word[i] == x):
                guess[i] = x
        if '_' not in guess:
            b = True
if '_' not in guess:
    print("Your guess is correct!")
    print("The word is",''.join(guess))