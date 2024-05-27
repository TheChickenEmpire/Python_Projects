from random import choice
while True:
    words = 'python', 'world', 'story', 'chipbot', 'time', 'cars', 'planes', 'garment', 'busting', 'stocker', 'unpoetical', 'impastured', 'witherband', 'bankership', 'wolf', 'packed', 'dog', 'refloating', 
    word = choice(words)
    display = len(word)*"_"
    letters = list(word)
    lives = 5
    guessed = ""
    print("The word is "+ str(len(word)) +" letters long you have 5 lives and one full word guess\nWarning!!!\nIf you Do a full word and it is not right you instantly lose\nGood luck\n")
    while True:
        lives = int(lives)
        if display == word:
            print("You win!\nThe word is "+word+"\nGreat job!")
            break
        if lives == 0:
            print("You lose the word was "+word)
            break
        print(display)
        guess = input("Guess:\n")
        if len(guess) == 1:
            if guess in letters:
                letters.remove(guess)
                index = word.find(guess)
                display = display[:index] + guess + display[index + 1:]
                guessed = guessed + guess +","

            elif guess in guessed:
                print("Already guessed")
                
            else:
                lives = lives - 1
                lives = str(lives)
                print("Letter not in word "+lives+" trys left")
                lives = int(lives)
                guessed = guessed + guess +","
        else:
            if guess == word:
                print("You win!\nThe word is "+word+"\nGreat job!")
                break
            else:
                print("You lose!\n the word was "+word)
                break
    while True:
        yn = input("Would you like to play again 1 for yes 2 for no:\n")
        if yn == '2':
            print("Bye!")
            exit()
        elif yn == '1':
            break
        else:
            pass