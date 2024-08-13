from translate import Translator
while True:
    try:
        translator = Translator(to_lang='English', from_lang='French')
        Subject = input("Input Contents: ")
        translation = translator.translate(Subject)
        print(translation)
    except:
        print("Failed to connect")