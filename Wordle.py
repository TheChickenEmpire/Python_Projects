import random
words = 'python', 'google', 'vscode'
while True:
    word = random.choice(words)
    letters = list(word)
    print(word)
    tries = 6
    print('The word has '+str(len(word))+' letters\n❌ = wrong\n✅ = right\nI = in word')
    while True:
        if tries == 0:
            print('You lose! The word was '+word)
            break
        guess = input('Guess:\n')
        if guess == word:
            print('You win!')
            break
        elif len(guess) == len(word):
            display = ''
            trys = 0
            for letterr in letters:
                lenth = len(guess)
                now = letters[trys]
                letter = guess[trys]
                if now not in letters:
                    display = display + '❌'
                elif now == letter:
                    display = display + '✅'
                elif now in letters:
                    display = display + 'I'
                trys = trys + 1
                print(display)
            tries = tries - 1
        else:
            print('Not long enough')
    while True:
        ask = input("Do you want to play again? \n1 = Yes\n2 = No\n")
        if ask == 1:
            break
        elif ask == 2:
            exit()