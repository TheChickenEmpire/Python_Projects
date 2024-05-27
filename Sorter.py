while True:
    words = input("Words split by space:\n").split(" ")
    words.sort()
    words = str(words)
    words = words.replace("[", "")
    words = words.replace("]", "")
    words = words.replace("'", "")
    print(words)