import speech_recognition as sr
import pyttsx3
from datetime import datetime
import AppOpener
import random
import PySimpleGUI as sg
import os
import requests
import string
from translate import Translator
import pyjokes
import webbrowser
import ctypes
import winshell
import segno
import cv2
from screen_brightness_control import set_brightness
from word2number import w2n
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np
try:
    open('chipbot_voice_set', 'r').close()
except FileNotFoundError:
    with open("chipbot_voice_set", 'a') as n:
        n.write('1')
with open("chipbot_voice_set", 'r') as n:
    if n.read() != '1' and n.read != '2':
        with open("chipbot_voice_set", 'a') as n:
            n.write('1')
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
        speak("Path to file")
        filename = input('Path to File: ')                                                                                                                                                                      
        word_count = count_words(filename)
        if word_count:
            speak(word_count)
            speak("are in this file")
            print("Number of Words in the file:", word_count)
            break
        else:
            speak("File not found")

def speak(*text):
    with open("chipbot_voice_set", 'r') as n:
        data = int(n.read())
        text = str(text)
        text = text.replace(',', '')
        engine = pyttsx3.init()
        voices = engine.getProperty("voices")
        engine.setProperty('voice', voices[data].id)
        engine.say(text)
        engine.runAndWait()

def change_speech():
    with open("chipbot_voice_set", 'r') as n: 
        with open("chipbot_voice_set", 'a') as h:
            if n.read() == '1':
                open('chipbot_voice_set', 'w').close()
                h.write('0')
            else:
                open('chipbot_voice_set', 'w').close()
                h.write('1')

def setsound(desired_vol):
    try:
        desired_vol = w2n.word_to_num(desired_vol)
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        vol_range = volume.GetVolumeRange()
        min_vol = vol_range[0]
        max_vol = vol_range[1]
        desired_vol_db = np.interp(desired_vol, [0, 100], [min_vol, max_vol])
        volume.SetMasterVolumeLevelScalar(desired_vol / 100, None)
        curr_vol = int(volume.GetMasterVolumeLevelScalar() * 100)
        speak(f'Volume set to: {int(curr_vol)} %')
    except():
        speak('Non valid volume')

def listen():
    while True:
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print("You said:", query)
            return query.lower()

        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Could you please repeat?")
            
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            speak(f"Could not request results from Google Speech Recognition service; {e}")
            exit()

def listen2():
    while True:
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)
            audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio)
            return query.lower()

        except sr.UnknownValueError:
            pass
            
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            speak(f"Could not request results from Google Speech Recognition service; {e}")
            exit()

def main():
    currentDateAndTime = datetime.now()
    current_time = currentDateAndTime.strftime("%H:%M:%S")
    if current_time < "12:00":
        speak(f"Good morning!")
    elif "12:00" <= current_time < "18:00":
        speak(f"Good afternoon!")
    else:
        speak(f"Good evening!")
    speak("how can i help you today?")
    while True:
        while True:
            c = listen2()
            if 'hey' in c or 'chip' in c or 'bot' in c:
                break
        speak('what')
        command = str(listen())

        if "hello how are you" in command:
            speak("Good How are you?")
            listen()
            speak("Okay great")

        elif "hello" in command:
            speak("Hi")

        elif "what's your name" in command:
            speak("I'm Chip bot voice assistant.")

        elif "exit" in command:
            speak("Goodbye!")
            break

        elif "what's the time" in command:
            currentDateAndTime = datetime.now()
            currentTime = currentDateAndTime.strftime("%H:%M:%S")
            speak("The times "+currentTime )
            
        elif 'hi' in command:
            speak("Hi")

        elif 'open google' in command:
            speak("Opening google")
            webbrowser.open("https://www.google.com/")

        elif 'open youtube' in command:
            speak("Opening youtube")
            webbrowser.open("https://www.youtube.com/")

        elif "what's the date" in command:
            today = datetime.today()
            today = today.strftime("%m/%d/%Y")
            speak("Today is "+ today)

        elif 'Excuse me' in command:
            speak("Yeah")

        elif "what are you doing" in command:
            speak("I am just waiting")

        elif "what are you" in command:
            speak("Im Chipbot")

        elif 'tell me' and 'joke' in command:
            speak(pyjokes.get_joke())

        elif "do you have a job" in command:
            speak("Yes a 24/7 job to listen to you")

        elif "go to ohio" in command:
            speak("bye i need to go catch the plane")
            exit()

        elif "whats up" in command:
            speak("not much")

        elif "open calculator" in command:
            speak("Opening calculater")
            sg.theme('Dark Gray 13')

            output = ''

            layout = [[sg.Text('Calculator')],
                    [sg.Text('', size=(10), key='output', expand_x=True)],
                    [sg.Button ('7'), sg.Button ('8'), sg.Button ('9')],
                    [sg.Button ('4'), sg.Button ('5'), sg.Button ('6')],
                    [sg.Button ('1'), sg.Button ('2'), sg.Button ('3')],
                    [sg.Button ('0'), sg.Button ('+'), sg.Button ('-')],
                    [sg.Button ('*'), sg.Button ('/'), sg.Button ('=')],
                    [sg.Button ('.'), sg.Button ('π'),sg.Button ('del'), sg.Button ('Clear')],]

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

        elif "bye" in command:
            speak("bye bye")
            break

        elif "open button" in command:
            speak("opening button")
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
                    
        elif "clear terminal" in command:
            os.system('cls' if os.name == 'nt' else "printf '\033c'")
            speak("cleared terminal")

        elif "greetings" in command:
            speak("greetings")

        elif "what's the weather" in command:
            while True:
                api_key = "6a9e388186982da3ed5365b65b9f9d4d"
                base_url = "http://api.openweathermap.org/data/2.5/weather?"
                speak("Location name")
                city_name = listen()
                if city_name == '':
                    pass
                else:    
                    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
                    response = requests.get(complete_url)
                    data = response.json()
                    if data["cod"] != "404":
                        main_info = data["weather"][0]["main"]
                        description = data["weather"][0]["description"]
                        temperature = data["main"]["temp"]
                        humidity = data["main"]["humidity"]
                        temperature = temperature - 273.15
                        print("Weather in " + city_name + ":")
                        print("Main Weather:", main_info)
                        print("Description:", description)
                        print("Temperature:", temperature, "C")
                        print("Humidity:", humidity, "%")
                        speak("Weather in")
                        speak(city_name)
                        speak("Main Weather")
                        speak(main_info)
                        speak("Description")
                        speak(description)
                        speak("Temperature")
                        speak(temperature)
                        speak("Celsius")
                        speak("Humidity")
                        speak(humidity)
                        speak("%")
                        break
                    else:
                        speak("City not found")
                        break

        elif "Translator" in command:
            speak("Say language to translate to")
            lan = listen()
            translator = Translator(to_lang=lan)
            speak("Stuff to translate")
            Subject = listen()
            translation = translator.translate(Subject)
            print(translation)

        elif "generate password" in command:
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(15))
            print("Password: "+ password)
            speak("Your password is")
            speak(password)
            
        elif "open " in command:
            app = command.replace("open ", "")
            AppOpener.open(app, match_closest=True)
            speak("Opened")
            speak(app)

        elif "search up " in command:
            search = command.replace("search up ", "")
            speak("searching")
            webbrowser.open(search)

        elif 'lock device' in command:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'lock the device' in command:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'lock my device' in command:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif "shut down device" in command:
            speak("closing the device")
            os.system('shutdown -s')
            
        elif "empty" and "bin" in command:
            try:
                winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                speak("Recycle Bin Recycled")
            except:
                pass

        elif "write a note" in command:
            speak("what should i write")
            note = listen()
            speak("should i include date and time")
            yn = str(listen())
            yn = yn.lower()
            try:
                if 'yes' in yn:
                    currentDateAndTime = datetime.now()
                    currentTime = currentDateAndTime.strftime("%H:%M:%S")
                    today = datetime.today()
                    today = today.strftime("%d/%m/%Y")
                    now = currentTime + " " + today
                    with open('Chipbot.txt', 'a') as fp:
                        fp.write(now + ":")
                        fp.write('\n')
                        fp.write(note)
                        fp.write('\n')
                        fp.write('\n')
                else:
                    with open('Chipbot.txt', 'a') as fp:
                        fp.write(note)
                        fp.write('\n')
                speak("note written")
            except:
                speak("error")

        elif "read" in command and "note" in command:
            try:
                speak("reading notes")
                with open("Chipbot.txt") as r:
                    s = r.read()
                    print(s)
                    speak(s)
            except:
                speak("Looks like you have not created one yet say write a note to create one")

        elif "make a qr code" in command:
            try:
                speak("Say content")
                code = listen()
                qrcode = segno.make_qr(code)
                qrcode.save(
                    "Qr code.png",
                    scale=100,
                )
                speak("QR code created")
            except:
                speak("error")

        elif "create a dice" in command:
            with open('Dice.py', 'a') as dw:
                dw.write("import random \nprint(random.randint(1, 6))")
        
        elif "make a dice" in command:
            speak('Made dice')
            with open('Dice.py', 'a') as dw:
                dw.write("import random \nprint(random.randint(1, 6))")
        
        elif "make a coin" in command:
            speak('Made coin')
            with open('Coin.py', 'a') as dw:
                dw.write("from random import choice\ncoin = 'Heads', 'Tails'\nprint(choice(coin))")

        elif "create a coin" in command:
            speak('Made coin')
            with open('Coin.py', 'a') as dw:
                dw.write("from random import choice\ncoin = 'Heads', 'Tails'\nprint(choice(coin))")

        elif 'roll a dice' in command:
            speak("rolling dice")
            speak(random.randint(1, 6))

        elif 'flip a coin' in command:
            speak("flipping coin")
            coin = 'Heads', 'Tails'
            speak(random.choice(coin))

        elif 'delete file' in command:
            try:
                speak("Input file to delete")
                f = input("File:")
                os.remove(f)
            except(FileNotFoundError):
                speak("File not found")

        elif 'word counter' in command:
            word_counter()

        elif 'take a picture' in command or 'take a photo' in command:
            speak('Taking a picture')
            camera_port = 0
            camera = cv2.VideoCapture(camera_port)
            return_value, image = camera.read()
            cv2.imwrite("picture.jpg", image)
            camera.release()
            speak('Done')
            
        elif 'set brightness to ' in command:
            command = str(command)
            brightness = command.replace('set brightness to ', '')
            try:
                brightness = w2n.word_to_num(brightness)
                set_brightness(brightness)
                speak("brightness set to ")
                speak(brightness)
            except:
                speak("Non valid brighteness")
        elif 'good morning' in command:
            speak("You to")

        elif 'good afternoon' in command:
            speak("you to")

        elif 'good evening' in command:
            speak("you to")
        
        elif 'good evening' in command:
            speak("you to")
            
        elif 'change voice' in command:
            change_speech()
            n.close()
            speak('changed voice')

        elif 'set volume to ' in command:
            command = command.replace('set volume to ', '')
            setsound(command)
            
        elif 'tell them' in command:
            speak('Subscribe to The Chicken Empire')

        else:
            speak("I am sorry I don't know what you mean")
            with open('Chipbot voice assistant Errors.txt', 'a') as fw:
                fw.write(command + '\n')
if __name__ == '__main__':
    main()