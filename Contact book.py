while True:
    print("1 to create contact \n2 to read contacts")
    what = input()
    if what == '1':
        phone_number = input("Phone Number: ")
        user = input("Person name: ")
        user = user + ":"
        with open('Phone_Number_Database.txt', 'a') as P:
            P.write(user + "\n" + phone_number+"\n\n")

    elif what == '2':
        with open('Phone_Number_Database.txt', 'r') as P:
            print("Contacts:\n"+P.read()+"\n\n")

    else:
        print("Non-Valid Input")