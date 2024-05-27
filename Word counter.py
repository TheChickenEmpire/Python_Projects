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
if __name__ == '__main__':
    word_counter()