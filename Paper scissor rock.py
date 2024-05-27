import random

def play_game():

    move_not_selected = True
    while(move_not_selected):
        player_input = input("Rock, Paper, Scissors: ")
        player_input = player_input.lower()
        if player_input == "apple":
            print ("A apple a keeps the doctor away")
        if (player_input == "rock" or player_input == "paper" or player_input == "scissors"):
            move_not_selected = False

    computer_move = random.randint(0,2)
    if(computer_move == 0):
        computer_move = "rock"
    elif(computer_move == 1):
        computer_move = "paper"
    elif(computer_move == 2):
        computer_move = "scissors"
    
    if (player_input == "rock" and computer_move == "rock"):
        print ("Computer chose Rock, It's a Draw")
    elif (player_input == "rock" and computer_move == "paper"):
        print ("Computer chose Paper, You Lose")
    elif (player_input == "rock" and computer_move == "scissors"):
        print ("Computer chose Scissors, You Win")
      
    elif (player_input == "paper" and computer_move == "rock"):
        print ("Computer chose Rock, You Win")
    elif (player_input == "paper" and computer_move == "paper"):
        print ("Computer chose Paper, It's a Draw")
    elif (player_input == "paper" and computer_move == "scissors"):
        print ("Computer chose Scissors, You Lose")
    
    elif (player_input == "scissors" and computer_move == "rock"):
        print ("Computer chose Rock, You Lose")
    elif (player_input == "scissors" and computer_move == "paper"):
        print ("Computer chose Paper, You Win")
    elif (player_input == "scissors" and computer_move == "scissors"):
        print ("Computer chose scissor, It's a Draw")
    print("Started New Game")
while(True):
    play_game()