from os import system
import random
from time import sleep as sp
allfighters = 'Hen', 'Llama', 'Sheep',
health = '110', '150', '90', 
abilities = 'Peck', 'Spit', 'Ram',
damage = '30', '20', '40', 
block = '20', '15', '10'
while True:
    choosen = input(f'Choose your fighter: {allfighters}\n').capitalize()
    if choosen in allfighters:
        system('cls')  
        break
    else:
        print('Non-valid input')
choosenint = allfighters.index(choosen)
choosenhealth = health[choosenint]
choosenability = abilities[choosenint]
choosendamage = damage[choosenint]
choosenblock = block[choosenint]
print(f"""You have choosen:
{choosen}
Health:
{choosenhealth}
Ability:
{choosenability}
Damage:
{choosendamage}""")
sp(5)
system('cls')
allenemyfighters = 'Bat', 'Skunk', 'Hedgehog', 'Weasel',
enemyhealth = '100', '130', '170', '60',
enemyabilities = 'Scare', 'Fart', 'Spike', 'Bite',
enemydamage = '50', '30', '60', '70',
enemyblock = '10', '10', '20', '10',
while True:
    enemyblock = '10', '10', '20', '10',
    choosenint = int(random.randint(0, 3))
    choosenenemy = allenemyfighters[choosenint]
    enemychoosenhealth = int(enemyhealth[choosenint])
    enemychoosenability = enemyabilities[choosenint]
    enemychoosendamage = int(enemydamage[choosenint])
    enemyblock = int(enemyblock[choosenint])
    choosenint = int(allfighters.index(choosen))
    choosenhealth = int(health[choosenint])
    choosenability = abilities[choosenint]
    choosendamage = int(damage[choosenint])
    choosenblock = int(block[choosenint])
    print(f'You are versing {choosenenemy}')
    enemymove = ''
    while True:
        if choosenhealth <= 0:
            print('You lose!')
            break
        if enemychoosenhealth <= 0:
            print('YOU WIN!!!')
            break
        while True:
            yourmove = input(f'Your turn! \nChoose to Block or attack!\n').lower()
            if yourmove == 'attack':
                print(f'{choosen} uses {choosenability}')
                damagenow = choosendamage
                if enemymove == 'block':
                    damagenow = choosendamage-enemyblock
                enemychoosenhealth = enemychoosenhealth-damagenow
                print(f'You dealt {damagenow} damage')
                break
            elif yourmove == 'block': 
                print('Hen uses block')
                break
            else:
                print('Invalid option')
                sp(1)
                system('cls')
        if choosenhealth <= 0:
            print('You lose!')
            break
        if enemychoosenhealth <= 0:
            print('YOU WIN!!!')
            break
        print(f'Your health: {choosenhealth}\nEnemy health: {enemychoosenhealth}')
        sp(4)
        system('cls')
        enemymove = random.randint(0, 1)
        if enemymove == 0: 
            enemymove = 'attack'
            if yourmove == 'block':
                damamageh = enemychoosendamage-choosenblock
                if damamageh > 0:
                    choosenhealth = choosenhealth - enemychoosendamage + choosenblock
                else:
                    damamageh = 0
            else:
                choosenhealth = choosenhealth - enemychoosendamage
                damamageh = enemychoosendamage
            print(f'{choosenenemy} uses {enemychoosenability}')
            print(f'Enemy dealt {damamageh} damage')
        else: 
            enemymove = 'block'
            print('Enemy uses block!')
        if choosenhealth <= 0:
            print('You lose!')
            break
        if enemychoosenhealth <= 0:
            print('YOU WIN!!!')
            break
        print(f'Your health: {choosenhealth}\nEnemy health: {enemychoosenhealth}')
        sp(4)
        system('cls')
    sp(4)
    system('cls')