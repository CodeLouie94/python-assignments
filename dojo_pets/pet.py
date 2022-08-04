from ninja import Ninja

class Pet:
    def __init__(self, name, type, tricks, health = 50, energy = 50):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep():
        pass

    def eat():
        pass

    def play():
        pass

    def noise():
        pass
    

class Cat(Pet):
    def __init__(self, name, type, tricks, health):
        super().__init__(name, type, tricks, health)
    


pet1 = Pet('Scooby', 'Great Dane', "sit")
pet2 = Pet('Bruno', 'Yorkshire', 'roll-over')
pet3 = Cat('Gary', 'Snail Cat','Purr', 25)


nin1 = Ninja('Shaggy', 'Norville', 'scooby snacks', 'bone', pet1)
nin2 = Ninja('Louie', 'Montilla', 'Nudges', 'Pedigree', pet3)


nin1.walk()
nin2.check_health()

nin2.walk()