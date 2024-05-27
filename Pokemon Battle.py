import random
import time as te
from dataclasses import dataclass
@dataclass
class Move():
    name: str
    damage: int
    mvtype:str

class pokemon():
    def __init__(self, name: str, health: int, pktype: str, move: Move):
        self.name = name
        self.health = health
        self.pktype = pktype
        self.move = move
    def __str__(self) -> str:
        return("Name: " + self.name + "\n" + "Health: " + str(self.health) + "\n" + "Type: " + self.pktype + "\n" + "Move: " + self.move.name)

    def take_damage(self, damage):
        self.health -= damage
    def Fainted(self):
        if self.health < 1:
            return True
        else:
            return False

Power_of_11_Flaps = Move("Power of 11 flaps", 22000, "Normal")
Chicken_Empire = pokemon("Chicken_Empire", 111111, "Normal/Flying", Power_of_11_Flaps)
Spit = Move("Spit", 9999, "Normal")
Alpaca_Empire = pokemon("Alpaca_Empire", 110000, "Normal", Spit)
current_pokemon = Chicken_Empire
Enemy_pokemon = Alpaca_Empire
while True:
    if(random.randint(0, 1)) == 1:
        Enemy_pokemon.take_damage(current_pokemon.move.damage)
        print(current_pokemon.name + " used " + current_pokemon.move.name)
        print(Enemy_pokemon.name + " took " + str(current_pokemon.move.damage) + " damage")
        print(Enemy_pokemon.name + " has " + str(Enemy_pokemon.health) + " hp left")
    else:
        print(current_pokemon.name + " missed")
    if Enemy_pokemon.Fainted():
        print(current_pokemon.name + " wins")
        break
    if current_pokemon == Chicken_Empire:
        current_pokemon = Alpaca_Empire
        Enemy_pokemon = Chicken_Empire
    elif current_pokemon == Alpaca_Empire:
        current_pokemon = Chicken_Empire
        Enemy_pokemon = Alpaca_Empire
    te.sleep(3)
    print("")
