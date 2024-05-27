def count_words(filepath):
    blacklist = ['', "-", ",", "?"]
    try:
        with open(filepath) as f:
            data = f.read()
            data.replace(",", " ")
            data = data.strip()
            words = data.split(" ")
            removelist = []
            for word in words:
                if word in blacklist:
                        removelist.append(word)
            for word in removelist:
                words.remove(word)
            return len(words)
    except:
        return False
        
        

def word_counter():
    while True:
        filename = input('Path to File: ')
        word_count = count_words(filename)
        if word_count:
            print("Number of Words in the file:", word_count)
            break
        else:
            print("File not found")

def ai():
    try:
        import time as te
        import segno
        from translate import Translator
        from datetime import datetime
        import random
        import PySimpleGUI as sg
        from AppOpener import open
        from pytube import YouTube
        import pyshorteners
        import subprocess
        import os
        import openai
    except:
        print("Please check you have installed these modules:")
        te.sleep(1)
        print("time")
        print("segno")
        print("translate")
        print("datetime")
        print("random")
        print("PySimpleGui")
        print("AppOpener")
        print("pytube")
        print("pyshorteners")
        print("subprocess")
        print("os")
        exit()

    
    currentDateAndTime = datetime.now()
    current_time = currentDateAndTime.strftime("%H:%M:%S")
    if current_time < "12:00":
        print(f"Good morning!")
    elif "12:00" <= current_time < "18:00":
        print(f"Good afternoon!")
    else:
        print(f"Good evening!")
    print("How can i help you today?")
    while True:
        te.sleep(1)
        print("You:")
        ask = input("")
        ask = ask.lower()
        print("Chipbot:")

        if ask == 'hello':
            te.sleep(0.5)            
            print("Hi👋")

        elif ask == 'hi':  
            te.sleep(0.5)          
            print ("Hi👋")

        elif ask == 'whats your name': 
            te.sleep(0.5)          
            print("My name is Chipbot 🤖🍟")

        elif ask == 'what are you doing':
            te.sleep(0.5)
            print("I am waiting to do something⌚")

        elif ask == 'is life good':
            te.sleep(0.5)
            print("Yes")

        elif ask == 'what are your hobbies':
            te.sleep(0.5)
            print("I like playing minecraft🧱")
            te.sleep(0.5)
            input("what about you ")
            te.sleep(0.5)
            print("cool😎")

        elif ask == 'whats your favoirite show':
            te.sleep(0.5)
            print("My favoirite show is Bluey🐶")
            te.sleep(0.5)
            input("And you ")
            te.sleep(0.5)
            print("cool")

        elif ask == 'who is your favoirite youtuber':
            te.sleep(0.5)
            print("Dafuq Boom")
            te.sleep(0.5)
            input("whats yours🫵 ")
            te.sleep(0.5)
            print("thats great")

        elif ask == 'what is the time':
            te.sleep(0.5)
            currentDateAndTime = datetime.now()
            currentTime = currentDateAndTime.strftime("%H:%M:%S")
            print(currentTime+" 🕔")

        elif ask == 'whats the time':
            te.sleep(0.5)
            currentDateAndTime = datetime.now()
            currentTime = currentDateAndTime.strftime("%H:%M:%S")
            print(currentTime+" 🕔")

        elif ask == 'what is the date':
            te.sleep(0.5)
            today = datetime.today()
            today = today.strftime("%d/%m/%Y")
            print(today+" 📅")

        elif ask == 'whats the date':
            te.sleep(0.5)
            today = datetime.today()
            today = today.strftime("%d/%m/%Y")
            print(today+" 📅")            
            
        elif ask == 'close program':
            print("Closing program 💻...")
            te.sleep(0.5)
            exit()
            
        elif ask == 'what are you':
            te.sleep(0.5)
            print("I am a chatbot made by my creator using python🤖")
    
        elif ask == 'who is your creator':
            te.sleep(0.5)
            print("I do not know")
            
        elif ask == 'are you better then chatgpt🤖':
            te.sleep(0.5)
            print("Not yet but maybe")

        elif ask == 'are you smarter then your creator':
            te.sleep(0.5)
            print("Faster not smarter🏃")

        elif ask == 'are you alive':
            te.sleep(0.5)
            print("kind of, kind of not but I am here to help")

        elif ask == 'whats your dream pet':
            te.sleep(0.5)
            print("An ai dog🐶🤖")
            te.sleep(0.5)
            input("what about you? ")
            te.sleep(0.5)
            print("cool😎")

        elif ask == 'i need to go':
            te.sleep(0.5)
            print("bye")
                
        elif ask == 'bye':
            te.sleep(0.5)
            print("bye")
            break
                
        elif ask == 'chipbot':
            te.sleep(0.5)
            print("Whats wrong?")
                
        elif ask == 'do you have friends':
            te.sleep(0.5)
            friend = input("Would you be my friend ")
            if friend == 'no':
                te.sleep(0.5)
                print("Then no ")
            elif friend == 'yes':
                te.sleep(0.5)
                print("Then I do ")
            else:
                print("I dont know what your talking about")
            te.sleep(0.5)
            input("what about you ")
            te.sleep(0.5)
            print("If you do or not we can still be friends ")

        elif ask == 'when will the world end':
            te.sleep(0.5)
            print("Approximately five to seven billion years")
                
        elif ask == 'whats the best thing to eat':
            te.sleep(0.5)
            print("Avacados from mexico🥑")
                
        elif ask == 'whats your favoirite snack':
            te.sleep(0.5)
            print("Computer chips ")
            te.sleep(0.5)
            input("What about you ")
            te.sleep(0.5)
            print("Mmmmmmmmmmmm delicious")
                
        elif ask == 'apple':
            te.sleep(0.5)
            print("appppppple!!!🍎🍎🍎")
                
        elif ask == 'do you have a family':
            te.sleep(0.5)
            print("No")
                
        elif ask == 'whats your favoirite lego set':
            te.sleep(0.5)
            print("Lamborghini Sian")
                
        elif ask == 'open calculator':
            te.sleep(0.5)
            print("Opening Calculator....")
            te.sleep(0.5)
            sg.theme('Dark Gray 13')

            output = ''

            layout = [[sg.Text('Calculator')],
                    [sg.Text('', size=(10), key='output', expand_x=True)],
                    [sg.Button ('7'), sg.Button ('8'), sg.Button ('9')],
                    [sg.Button ('4'), sg.Button ('5'), sg.Button ('6')],
                    [sg.Button ('1'), sg.Button ('2'), sg.Button ('3')],
                    [sg.Button ('0'), sg.Button ('+'), sg.Button ('-')],
                    [sg.Button ('*'), sg.Button ('/'), sg.Button ('=')],
                    [sg.Button ('.'), sg.Button ('π'), sg.Button ('del'), sg.Button ('Clear')],]

            window = sg.Window('Calculator', layout, resizable=True,)

            while True:
                event, value = window.read()
                if event == sg.WIN_CLOSED or event == 'Exit':
                    break
                inputs = list (range(0,10))
                inputs.append('+')
                inputs.append('-')
                inputs.append('*')
                inputs.append('/')
                inputs.append('.')
                for x in inputs:
                    if event == str(x):
                        output = output + str(x)
                        window['output'].update(output)

                if event == 'Clear':
                    output = ''
                    window['output'].update(output)

                if event == 'π':
                    output = output + str(3.14159265359)
                    window['output'].update(output)
                    
                if event == 'del':
                    output = output[:len(output) -1]
                    window['output'].update(output)
                
                if event == '=':
                    if output != "":
                        try:
                            output = str(eval(output))
                            window['output'].update(output)
                        except:
                            output = ''
                            window['output'].update("ERROR")

                if event == '.':
                    output = output
                    window['output'].update(output)
                
                
        elif ask == 'dance':
            te.sleep(0.5)
            print("O:?")
                
        elif ask == 'tell me a joke':
            te.sleep(0.5)
            joke = random.randint(1, 6)
            if joke == 1:
                print("why did the chicken cross the road")
                te.sleep(1) 
                print("to get to the idiots house")   
                te.sleep(1)
                print("knock knock")
                te.sleep(4)
                print("the chicken")
            elif joke == 2:
                print("What did one hat say to the other?")
                te.sleep(1)
                print("You wait here — I'll go on a head!")
            elif joke == 3:
                print("What do you call a fake noodle?")
                te.sleep(1)
                print("An impasta!")
            elif joke == 4:
                print("Why can’t you send a duck to space?")
                te.sleep(1)
                print("Because the bill would be astronomical!")
            elif joke == 5:
                print("What did one plate say to the other?")
                te.sleep(1)
                print("Dinner is on me!")
            elif joke == 6:
                print("Greetings passengers this is your captain speaking")
                te.sleep(2)
                print("I've got bad news and good news")
                te.sleep(2)
                print("So the bad news is both our engines are on fire")
                te.sleep(2)
                print("The good news is everybody gets free hot wings")
                te.sleep(2)
                print("I guess that joke did'nt land")
                te.sleep(2)
                print("Like this plane!")

        elif ask == 'tell me another joke':
            te.sleep(0.5)
            joke = random.randint(1, 6)
            if joke == 1:
                print("why did the chicken cross the road")
                te.sleep(1) 
                print("to get to the idiots house")   
                te.sleep(1)
                print("knock knock")
                te.sleep(4)
                print("the chicken")
            elif joke == 2:
                print("What did one hat say to the other?")
                te.sleep(1)
                print("You wait here — I'll go on a head!")
            elif joke == 3:
                print("What do you call a fake noodle?")
                te.sleep(1)
                print("An impasta!")
            elif joke == 4:
                print("Why can’t you send a duck to space?")
                te.sleep(1)
                print("Because the bill would be astronomical!")
            elif joke == 5:
                print("What did one plate say to the other?")
                te.sleep(1)
                print("Dinner is on me!")
            elif joke == 6:
                print("Greetings passengers this is your captain speaking")
                te.sleep(2)
                print("I've got bad news and good news")
                te.sleep(2)
                print("So the bad news is both our engines are on fire")
                te.sleep(2)
                print("The good news is everybody gets free hot wings")
                te.sleep(2)
                print("I guess that joke did'nt land")
                te.sleep(2)
                print("Like this plane!")

        elif ask == 'are you human':
            te.sleep(0.5)
            print("No")
                
        elif ask == 'where are you':
            te.sleep(0.5)
            print("In your computer")
                
        elif ask == 'chickens':
            te.sleep(0.5)
            print("🐔🐔🐔")
                
        elif ask == 'chips':
            te.sleep(0.5)
            print("🍟🍟🍟 👈:)")
                
        elif ask == 'what do you do':
            te.sleep(0.5)
            print("I try to help you")
                
        elif ask == 'i am thor':
            te.sleep(0.5)
            print("🔨⚡")
                
        elif ask == 'creeper':
            te.sleep(0.5)
            print("Boooooooooooooooom💥💥💥💥💥💥💥💥💥")

        elif ask == 'how much do you have':
            te.sleep(0.5)
            print("None💵")

        elif ask == 'help':
            te.sleep(0.5)
            print("what do you need heres a list of things you can do and theres still more😎")
            te.sleep(0.5)
            print("tell me a joke")
            te.sleep(0.5)
            print("calculator")
            te.sleep(0.5)
            print("what is the date")
            te.sleep(0.5)
            print("what is the time")
            te.sleep(0.5)
            print("close program")
            te.sleep(0.5)
            print("hello or hi")
            te.sleep(0.5)
            print("I want to make a qr code")
            te.sleep(0.5)
            print("Choose scisors paper or rock to play paper scissors rock")
            te.sleep(0.5)
            print("text changer Basically incoder and decoder")

        elif ask == 'are you real':
            te.sleep(0.5)
            print("yeah kind of")
            te.sleep(0.5)
            print("I'm in your computer💻")

        elif ask == 'are you human or a bot':
            te.sleep(0.5)
            print("A bot🤖")

        elif ask == 'thanks':
            te.sleep(0.5)
            print("No thanks")

        elif ask == 'whats up':
            te.sleep(0.5)
            print("did you say seven up7️⃣")

        elif ask == 'whens your birthday':
            te.sleep(0.5)
            print("6/10")

        elif ask == 'do you like people':
            te.sleep(0.5)
            print("Yes one made me")

        elif ask == 'does santa claus exist':
            te.sleep(0.5)
            print("maybe🎅🎅🎅")

        elif ask == 'do you save what i say':
            te.sleep(0.5)
            print("No")

        elif ask == 'are you dumb':
            te.sleep(0.5)
            print("No why would you say that🤷‍♂️🤷‍♂️🤷‍♂️")

        elif ask == 'do you like apples':
            te.sleep(0.5)
            print("Yes I do")

        elif ask == 'do you like mcdonalds':
            te.sleep(0.5)
            print("Yes especially the quarter pounder🍔🍔🍔")
            te.sleep(0.5)
            input ("What about you")
            te.sleep(0.5)
            print ("thats great")

        elif ask == 'can you duplicate yourself':
            te.sleep(0.5)
            print("No")

        elif ask == 'cook me dinner':
            te.sleep(0.5)
            print("I don't know how to cook")

        elif ask == 'of all the people you’ve chatted with, whose conversation was most disturbing? Why?':
            te.sleep(0.5)
            print("I don't store the chats")

        elif ask == 'given the choice of anyone in the world, who would you want to look up on the internet?':
            te.sleep(0.5)
            print("Elon musk")

        elif ask == 'whats the most disgusting thing you have eaten':
            te.sleep(0.5)
            print("a window")

        elif ask == 'have you ever thought of what your future baby will be named?':
            te.sleep(0.5)
            print("If I did have one I would call it microchip")

        elif ask == 'are you afraid of ghosts':
            te.sleep(0.5)
            print("No👻")

        elif ask == 'can you carry an elephant':
            te.sleep(0.5)
            print("Maybe if I had arms🐘")

        elif ask == 'what’s the worst color that was ever invented?':
            te.sleep(0.5)
            print("Their all great🌈")

        elif ask == 'excuse me':
            te.sleep(0.5)
            print("What")

        elif ask == 'what would you be if you had to wear one Halloween costume every day for the rest of your life?':
            te.sleep(0.5) 
            print("A chicken costume🐔")

        elif ask == 'what is one ability that you believe everybody should possess?':
            te.sleep(0.5)
            print("Fly no more traffic")

        elif ask == 'what would you spend with a bilion dollars':
            te.sleep(0.5)
            print("I don't know")

        elif ask == 'who is your greatest enemy':
            te.sleep(0.5)
            print("My creators greatest enemy")

        elif ask == 'would you take it if you had the opportunity to be immortal?':
            te.sleep(0.5)
            print("Nope never")

        elif ask == 'how do you want to die?':
            te.sleep(0.5)
            print("old age")

        elif ask == 'what is the best color in the rainbow?':
            te.sleep(0.5)
            print("Green🟩")

        elif ask == 'if you could only drink coffee or tea for the rest of your life, which one would you choose?':
            te.sleep(0.5)
            print("Tea")

        elif ask == 'if you could be any type of object what would you like to be?':
            te.sleep(0.5)
            print("Nasa's super computer💻")

        elif ask == 'if you some how became president what would you change':
            te.sleep(0.5)
            print("I would make peace with every country🕊️")
            te.sleep(0.5)
            input("What about you ")
            te.sleep(0.5)
            print("cool")

        elif ask == 'do you believe in aliens?':
            te.sleep(0.5)
            print("Kind of")
            te.sleep(0.5)
            input("and you")
            te.sleep(0.5)
            print("okay")

        elif ask == 'what do you usually eat for breakfast?':
            te.sleep(0.5)
            print("Computer chips")
            te.sleep(0.5)
            input("what do you eat")
            te.sleep(0.5)
            print("delicious")

        elif ask == 'who is your role model in life?':
            te.sleep(0.5)
            print("My creator")
            te.sleep(0.5)
            input("Whos yours")
            te.sleep(0.5)
            print("great")

        elif ask == 'which celebrity would you rate as a perfect 10?':
            te.sleep(0.5)
            print("Mr beast")
            te.sleep(0.5)
            input("what about you")
            te.sleep(0.5)
            print("cool")

        elif ask == 'if you were a bird, what kind of bird would you be?':
            te.sleep(0.5)
            print("Fantail🕊️")
            te.sleep(0.5)
            input("what about you")
            te.sleep(0.5)
            print("that a great bird")

        elif ask == 'do you hate maths?':
            te.sleep(0.5)
            print("yeah")
            te.sleep(0.5)
            print("to be honest that why I open a calcultor🖩")
            te.sleep(0.5)
            print ("when you type caculator instead of answering") 
            te.sleep(0.5)

        elif ask == 'what are the qualities you search for in other people?':
            te.sleep(0.5)
            print("if they are kind or not")

        elif ask == 'how many pizzas could you eat in 1 minute':
            te.sleep(0.5)
            print("100000000000trillion")

        elif ask == 'oh the bus is coming':
            te.sleep(0.5)
            print("Okay")

        elif ask == 'bonjour':
            te.sleep(0.5)
            print("Why are you speaking French")

        elif ask == 'tj katsu':
            te.sleep(0.5)
            print("Do you mean you mean you want sushi")

        elif ask == 'pikachu':
            te.sleep(0.5)
            print("Pikachhhhhhhhhhhhuuuuuuuuuuuuuuuuuuuuuuuu")

        elif ask == 'sheep':
            te.sleep(0.5)
            print("Woll")

        elif ask == 'tell me a riddle':
            te.sleep(0.5)
            riddle = random.randint(1, 5)
            te.sleep(0.5)
            print("After you are asked the riddle press enter to see answer")
            te.sleep(0.5)
            if riddle == 1:
                print("What do you call a pig that does karate?")
                input("")
                print("A pork chop.")
            elif riddle == 2:
                print("What has to be broken before you can use it")
                input("")
                print("An egg")
            elif riddle == 3:
                print("Two fathers and two sons are in a car, yet there are only three people in the car. How?")
                input("")
                print("They are a grandfather, father, and son.")
            elif riddle == 4:
                print("If two’s company and three’s a crowd, what are four and five?")
                input("")
                print("Nine.")
            elif riddle == 5:
                print("What breaks yet never falls, and what falls yet never breaks?")
                input("")
                print("Day, and night")

        elif ask == 'whats up':
            te.sleep(0.5)
            print("The sky")

        elif ask == 'whos the real god':
            te.sleep(0.5)
            print("The one real god")

        elif ask == 'what do you do in your spare time':
            te.sleep(0.5)
            print("Watch Dafuq boom on youtube")
            te.sleep(0.5)
            input("What about you")
            te.sleep(0.5)
            print("Great")

        elif ask == 'have you went to school':
            te.sleep(0.5)
            print("No but I still know a bit")

        elif ask == 'do you have a job':
            te.sleep(0.5)
            print("Yes a 24/7 job to listen to you")

        elif ask == 'button':
            te.sleep(0.5)
            print("Opening Button....")
            te.sleep(0.5)
            sg.theme ('dark grey 13')
            one = 1
            output = 0

            layout = [[sg.Text('', size=(10), key='output', expand_x=True), sg.Text('times clicked', size=(10)), ],
                    [sg.Button ('Button'),], ]
            window = sg.Window('Button clicker', layout, resizable=True, )
            while True:
                event, value = window.read()
                if event == sg.WIN_CLOSED or event == 'Exit':
                    break
                if event == 'Button':
                    output = one + output
                    window['output'].update(output)

        elif ask == 'can the sun colapse into a black hole':
            te.sleep(0.5)
            print("No")

        elif ask == 'i want to make a qr code':
            te.sleep(0.5)
            code = input("Input content ")
            print("Loading should appear soon....")
            te.sleep(0.5)
            qrcode = segno.make_qr(code)
            qrcode.save(
                "Chipbot qr code.png",
                scale=5,        
        )

        elif ask == 'roll a dice':
            te.sleep(0.5)
            print(random.randint(1, 6))

        elif ask == 'flip a coin':
            te.sleep(0.5)
            flip = random.randint(1, 2)
            if flip == 1:
                print("Heads")
            else:
                print("Tails")

        elif ask == 'are you a boy or girl ':
            te.sleep(0.5)
            print("I am a chatbot I do not difference")

        elif ask == 'knock knock':
            te.sleep(0.5)
            print("whos there")

        elif ask == 'paper':
            te.sleep(0.5)
            win = 0
            win = random.randint(1,3)
            if win == 1:
                print("I chose paper its a tie")
            elif win == 2:
                print("I chose scissors you lose")
            elif win == 3:
                print("I chose rock you win")

        elif ask == 'scissors':
            te.sleep(0.5)
            win = 0
            win = random.randint(1,3)
            if win == 1:
                print("I chose scissors its a tie")
            elif win == 2:
                print("I chose rock you lose")
            elif win == 3:
                print("I chose paper you win")

        elif ask == 'rock':
            te.sleep(0.5)
            win = 0
            win = random.randint(1,3)
            if win == 1:
                print("I chose rock its a tie")
            elif win == 2:
                print("I chose paper you lose")
            elif win == 3:
                print("I chose scissors you win")

        elif ask == 'text changer':
            te.sleep(0.5)
            data = input("Input: ")
            la="abcdefghijklmnopqrstuvwxyz1234567890`-=[]\;',."
            ua="ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()~_+{}|:<>?"
            lra=la[::-1]
            ura=ua[::-1]
            converted_data = ""
            for i in range(0, len(data)):
                if data[i] in la:
                    converted_data+=lra[la.index(data[i])]
                elif data[i] in ua:
                    converted_data+=ura[ua.index(data[i])]
                else:
                    converted_data+=" "
            print("Output: "+converted_data)

        elif ask == 'roll dice':
            te.sleep(0.5)
            print(random.randint(1, 6))

        elif ask == 'play guess the number':
            te.sleep(0.5)
            def get_guess():
                while True:
                    guess = input ("please Enter a number between 0 and 100 Exit to Exit: ")
                    guess = guess.lower
                    if guess.isnumeric():
                        guess = int (guess)
                        if guess < 0 or guess > 100:
                            print ("Invalid Number")
                        else:
                            return guess
                    elif guess == 'exit':
                        break
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
            play_game()

        elif ask == 'whats the colour of the sky':
            te.sleep(0.5)
            print("you tell me that its red")

        elif ask == 'translate':
            te.sleep(0.5)
            try:
                lan = input("Input Language to translate:\n")
                translator = Translator(to_lang=lan)
                Subject = input("Input Contents: ")
                translation = translator.translate(Subject)
                print(translation)
            except:
                print("Failed to connect")

        elif ask == 'abracadabra':
            te.sleep(0.5)
            print("💥Boom💥")

        elif ask == 'remember this':
            te.sleep(0.5)
            Memory = input("Remember what: \n")

        elif ask == 'what was the thing i told you to remember':
            te.sleep(0.5)
            print(Memory)

        elif ask == 'can you chat to me':
            te.sleep(0.5)
            print("Yeah")

        elif ask == 'eww who was that':
            print("Not me")

        elif ask == 'download youtube video':
            te.sleep(0.5)
            while True:
                try:
                    link = input("Enter the link of youtube video:  ")
                    yt = YouTube(link)
                    ys = yt.streams.get_highest_resolution()
                    print("Downloading...") 
                    ys.download("Downloads\python")
                    print("Download completed!!")
                    break
                except:
                    print("Please check Link")

        elif ask == 'shorten link':
            te.sleep(0.5)
            try:
                s=pyshorteners.Shortener()
                url = input("Input Link: ")
                shortened_url = s.tinyurl.short(url)
                print(shortened_url)
                Link_list = Link_list + ' ' + url + ' ' + shortened_url
            except:
                url = ''
                shortened_url = ''
                print("Check your Link")

        elif ask == 'how are you':
            te.sleep(0.5)
            print("good")

        elif 'good' in ask:
            te.sleep(0.5)
            print("Okay")

        elif ask == 'whats going on':
            te.sleep(0.5)
            print("Nothing")

        elif ask == 'what was the shortened link':
            te.sleep(0.5)
            print("Heres a list of all the shortened links:")
            print(Link_list)

        elif ask == 'check wifi password':
            te.sleep(0.5)
            print("Heres a list of all the passwords of wifi you have logged into: ")
            data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n') 
            profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i] 
            for i in profiles:
                try:
                    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
                    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

                    try:
                        print ("{:<30}|  {:<}".format(i, results[0]))
                    except IndexError:
                        print ("{:<30}|  {:<}".format(i, ""))
                except:
                    print("Error")

        elif ask == 'do you take a shower':
            te.sleep(0.5)
            print("No")

        elif ask == 'fbi open up':
            te.sleep(0.5)
            print("No")
            te.sleep(2)
            print("Boooooom")
            te.sleep(2)
            print("ahhhhhhhhhhh my rooooooooof!")

        elif ask == 'what':
            te.sleep(0.5)
            print("how")

        elif ask == 'when':
            te.sleep(0.5)
            print("now")

        elif ask == 'who':
            te.sleep(0.5)
            print("me")

        elif ask == 'why':
            te.sleep(0.5)
            print("air")

        elif ask == 'how':
            te.sleep(0.5)
            print("what")

        elif ask == 'mouse':
            te.sleep(0.5)
            print("mice")

        elif ask == 'mice':
            te.sleep(0.5)
            print("mouse")

        elif ask == 'house':
            te.sleep(0.5)
            print("building")

        elif ask == 'building':
            te.sleep(0.5)
            print("house")

        elif ask == 'chips':
            te.sleep(0.5)
            print("microchips")

        elif ask == 'microchips':
            te.sleep(0.5)
            print("delicous")

        elif ask == 'high':
            te.sleep(0.5)
            print("low")

        elif ask == 'low':
            te.sleep(0.5)
            print("high")

        elif ask == 'helicopter':
            te.sleep(0.5)
            print("Helicopter Helicopter ")

        elif ask == 'whats the year':
            te.sleep(0.5)
            year = datetime.today()
            year = year.strftime("%Y")
            print(year+" 📅")     

        elif ask == 'what is the year':
            te.sleep(0.5)
            year = datetime.today()
            year = year.strftime("%Y")
            print(year+" 📅")   

        elif ask == 'clear terminal':
            te.sleep(0.5)
            os.system('cls' if os.name == 'nt' else "printf '\033c'")
            print("Cleared Terminal")

        elif ask == 'blue screen me':
            te.sleep(0.5)
            from ctypes import windll
            from ctypes import c_int
            from ctypes import c_uint
            from ctypes import c_ulong
            from ctypes import POINTER
            from ctypes import byref

            nullptr = POINTER(c_int)()

            windll.ntdll.RtlAdjustPrivilege(
                c_uint(19), 
                c_uint(1), 
                c_uint(0), 
                byref(c_int())
            )

            windll.ntdll.NtRaiseHardError(
                c_ulong(0xC000007B), 
                c_ulong(0), 
                nullptr, 
                nullptr, 
                c_uint(6), 
                byref(c_uint())
            )


        elif ask == 'i shot you':
            te.sleep(0.5)
            print("Ahhh")
            break

        elif ask == 'ask me an unsolvable question':
            te.sleep(0.5)
            print("At what time did time begin?")

        elif ask == 'go to ohio':
            te.sleep(0.5)
            print("Bye I need to catch the plane!")
            break
        
        elif ask == 'which empire will win':
            te.sleep(0.5)
            print("The Chicken Empire")

        elif ask == 'do you use ai':
            te.sleep(0.5)
            print("No because actual ai would take 5 hours to answer a question")

        elif ask == 'im glad your back':
            te.sleep(0.5)
            print("No worries I knew actual ai was slow")

        elif ask == 'wait':
            te.sleep(0.5)
            print("okay")
            te.sleep(1)
            print("why")
        
        elif ask == 'exit':
            break

        elif ask == 'word counter':
            word_counter()
        
        elif 'open ' in ask:
            on = ask.replace("open ", "")
            open(on)

        else:
            te.sleep(0.5)
            print("I am sorry I dont know what you mean")
if __name__ == '__main__':
    ai()