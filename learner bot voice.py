import sys
import speech_recognition as sr
import pyttsx3
def speak(*text):
    text = str(text)
    text = text.replace(',', '')
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

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

def learner_bot():
    while True:
        try:
            def learn():
                while True:
                    import learner_bot_database
                    input("Enter To speak\n--------------\n")
                    Text = listen()
                    say = learner_bot_database.database(Text)
                    if say != None:
                        speak(say)
                    else:
                        speak("No answer found please provide answer for "+ Text + " or say No")
                        answer = listen()
                        wer = answer.lower()
                        if wer == "no":
                            pass
                        else:
                            ans = '"' + answer + '"'
                            Text = '"' + Text + '"'
                            with open('learner_bot_database.py', 'a') as dw:
                                dw.write("\n    elif Text == " + Text + ":\n        return " + ans + "\n")
                                del sys.modules['learner_bot_database']
            learn()
        except ModuleNotFoundError:
            with open('learner_bot_database.py', 'a') as dw:
                dw.write('def database(Text):\n    if Text == "hi":\n        return "Hi"\n')

        except SyntaxError:
            print("Remove last entered data from database immediately!!!")
            print("Last entered data contains characters that disturb code!!!")
            break

        except:
            print("Unknown Error Has Occured")
if __name__ == '__main__':
    learner_bot()