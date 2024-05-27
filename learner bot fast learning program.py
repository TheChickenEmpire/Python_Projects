import sys
while True:
    try:
        def learn():
                while True:
                    import learner_bot_database
                    Text = input("Question:\n")
                    Text = Text.lower()
                    say = learner_bot_database.database(Text)
                    if say != None:
                        pass
                    else:
                        answer = input("Answer:\n")
                        wer = answer.lower()
                        if wer == "":
                            pass
                        else:
                            ans = "'" + answer + "'"
                            Text = "'" + Text + "'"
                            with open('learner_bot_database.py', 'a') as dw:
                                dw.write("\n    elif Text == " + Text + ":\n        return " + ans + "\n")
                                del sys.modules['learner_bot_database']
        learn()
    except ModuleNotFoundError:
        with open('learner_bot_database.py', 'a') as dw:
            dw.write("def database(Text):\n    if Text == 'hi':\n        return 'Hi'\n")

    except SyntaxError:
        print("Remove last entered data from database immediately!!!")
        print("Last entered data contains characters that disturb code!!!")
        break

    except:
        print("Unknown Error Has Occured")