from string import ascii_letters as a
print('Welcome To LM')
print(15 * '_')
while True:
    n1 = input('Name1:\n')
    n2 = input('Name2:\n')
    n1 = list(n1)
    n2 = list(n2)
    n1 = n1[0].capitalize()
    n2 = n2[0].capitalize()
    if n1 in a and n2 in a:
        place1 = a.index(n1)
        place2 = a.index(n2)
        equal = place1 + place2
        final = str(equal / 2)
        if '.0' in final:
            print('Match :) :)')
        else:
            print('No match XXX')
    else:
        print('Is that a name???')
        print('\n')