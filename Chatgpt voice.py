import speech_recognition as sr
import pyttsx3
import openai
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

def main():
    speak("Hello! How can I help you today?")
    while True:
        input("Enter To speak\n--------------\n")
        command = listen()
        print("Generating.....")
        openai.api_key = "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"
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": command}])
        message = completion.choices[0].message.content
        print(message)
        speak(message)

if __name__ == "__main__":
    main()