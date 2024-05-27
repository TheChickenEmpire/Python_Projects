def SP(Names: str):
    """How to use Put names like this Sp("Lucas, Zhao")"""
    h=0
    Smashed = 0
    names = Names.split(', ')
    for name in names:
        Name = names[h]
        while True:
            yn = input('Smash or pass '+Name+':\n').lower()
            if yn == 'smash':
                Smashed = Smashed+1
                break
            elif yn == 'pass':
                break
            else:
                pass
        h=h+1
    if Smashed == h:
        print('Well done you got the best score possible!!!!!!!!!')
    else:
        print('Score: '+str(Smashed))
SP("Josie, Sarah, Beckett, Gigi")