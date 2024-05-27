import random

def get_guess():
    while True:
        guess = input ("please Enter a number between 0 and 100: ")
        if guess.isnumeric():
            guess = int (guess)
            if guess < 0 or guess > 100:
                print ("Invalid Number")
            else:
                return guess
        else:
            print("Please enter a Number")
def play_game():
    move = random.randint(0, 100)
    moves = 0
    while True:
        guess = get_guess()
        moves += 1
        if guess < move:
            print("guess is too Low")
        elif guess > move:
            print ("guess is too High")
        else:
            print("Correct guess")
            print("You took "+ str(moves) + " Guesses")
            break
while True:
    print("Started new Game")
    play_game()