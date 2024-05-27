import sys
def learner_bot():
    while True:
        try:
            def learn():
                while True:
                    import learner_bot_database
                    Text = input("You:\n")
                    Before = Text
                    Text = Text.lower()
                    say = learner_bot_database.database(Text)
                    if say != None:
                        print("Learner Bot:\n" + say)
                    else:
                        answer = input("No answer found please provide answer for "+ Before + " or type No: ")
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