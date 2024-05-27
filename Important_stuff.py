import speech_recognition as sr
import pyttsx3, requests
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

def weather(city_name):
    api_key = "6a9e388186982da3ed5365b65b9f9d4d"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        temperature = temperature - 273.15
        return description
def weather2(city_name):
    api_key = "6a9e388186982da3ed5365b65b9f9d4d"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        temperature = data["main"]["temp"]
        temperature = str(temperature - 273.15)
        temperature = list(temperature)
        temp = temperature[0] + temperature[1]
        return temp
def weather3(city_name):
    api_key = "6a9e388186982da3ed5365b65b9f9d4d"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        humidity = data["main"]["humidity"]
        return str(humidity)