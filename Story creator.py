from random import choice as ce
while True:
    Animal = "Chicken","Pig","Cow","Duck","Chick","Duckling","Dog","Cat","Kitten","Puppy","Lamb",
    Vehicle = "Car","Plane","Rocket","Boat","Train","Bus","Motorbike","SpaceShip",
    Family = "Mum","Dad","Grandma","Grandpa","Sister","Brother","Daughter","Son",
    Planet = "Venus","Mars","the Moon","the Sun","Mercury","Pluto","Saturn","Uranus","Jupiter",
    print("Once upon a time there was a", ce(Animal), "who had a", ce(Vehicle),"but did'nt know how to drive it\nSo he went to a special training ground to learn how to drive it he was suprised when the trainer\nwas his", ce(Family), " \nEventually He learned how to drive it but then he accidentaly pushed the eject button\nand flew out of the vehicle while driving it then it hit a speed bump and flew into",ce(Planet)," \nThen it bounced back And hit a poor Little", ce(Animal))
    yn = input("\nDo you want to generate another story\n")
    yn = yn.lower()
    if yn == 'no':
        break