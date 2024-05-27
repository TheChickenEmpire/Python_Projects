import pyshorteners
def shorten():
    while True:
        try:
            s=pyshorteners.Shortener()
            url = input("Input Link: ")
            shortened_url = s.tinyurl.short(url)
            print(shortened_url)
        except:
            url = ''
            shortened_url = ''
            print("Check your Link")
shorten()