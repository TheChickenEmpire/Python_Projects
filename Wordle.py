import random
words = 'python', 'google', 'vscode', 'Chicken', 'Cow', 'Empire', 'Subscribe', 'Like', 'Dxjames999', 'Zxjoshua33', 'Chatgpt', 'TheChickenEmpire',
while True:
    word = random.choice(words).lower()
    letters = list(word)
    tries = 6
    print('The word has '+str(len(word))+' letters\n❌ = wrong\n✅ = right')
    while True:
        if tries == 0:
            print('You lose! The word was '+word)
            break
        guess = input('Guess:\n').lower()
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
                if now == letter:
                    display = display + '✅'
                elif now in letters:
                    display = display + '❌'
                trys = trys + 1
            print(display)
            tries = tries - 1
        elif len(guess) > len(word):
            print('Too long')
        elif len(guess) < len(word):
            print('Too short')
    while True:
        ask = str(input("Do you want to play again? \n1 = Yes\n2 = No\n"))
        if ask == '1':
            break
        elif ask == '2':
            exit()