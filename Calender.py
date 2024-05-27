import calendar
while True:
    try:
        year = int(input("Year:\n"))
        Ye = year
        Ye = str(Ye)
        print("The calendar of year "+Ye+" is:")
        print(calendar.calendar(year))
    except:
        print("Non-Valid input")