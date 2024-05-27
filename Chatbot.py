import difflib
def chat(asks: str, ans: str):
    """Use this function for chatbots
    By typing for example chat('Hi, Hello',
                                                                                                Hi, Greetings)
    It will return the Answer of the closest question Line 1 is Questions 
    line 2 is answers"""
    asks = asks.split(', ')
    ans = ans.split(', ')
    ask = input('You:\n').lower()
    e = difflib.get_close_matches(ask, asks, 1)
    try:
        e = e[0]
        e = str(e)
        e = e.replace('[', '')
        e = e.replace(']', '')
        e = e.replace("'", '')
        index = asks.index(e)
        return('Chatbot:\n'+ans[index].capitalize())
    except:
        return("Im sorry I don't understand what you mean")
if __name__ == '__main__':
    while True:
        print(chat('hi, hello, whats up, hey, hows your day been, im good, where youve been, whos there, hows it going', 
                    'hi, hi, not much, what, good what about you, very good then, in your computer, me, good'))