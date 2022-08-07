import random

class Player:
    def __init__(self, name, strength = 15, speed = 2, health = 100):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.health = health

class Pirate(Player):
    def __init__( self , name ):
        super().__init__(name, 20, 3)
        


class Ninja(Player):
    def __init__(self, name):
        super().__init__(name, 10, 6)
        

class Game:
    def __init__(self, p1:Player, p2:Player):
        self.p1=p1
        self.p2=p2
        
    def battle(self):
        turn_count = 1
        while p1.health>0 and p2.health>0:
            print(f"***** Turn {turn_count} *****")
            if self.roll_dice() == "p2att":
                print(f"{p2.name} Attacks {p1.name}")
                self.p1.health-=self.p2.strength
            else:
                print(f"{p1.name} Attacks {p2.name}.")
                self.p2.health-=self.p1.strength
            self.show_stats()
            turn_count += 1
        print("********KO*********")
        if p1.health<=0:
            print(f"{p2.name} WINS")
        else:
            print(f"{p1.name} WINS")
        return self
    def roll_dice(self):
        p1_roll = random.randint(1, p1.speed)
        p2_roll = random.randint(1, p2.speed)
        if p1_roll == p2_roll:
            return self.roll_dice()
        elif p1_roll > p2_roll:
            return "p1att"
        else:
            return "p2att" 
    def show_stats(self):
        print(f" {self.p1.name}: {self.p1.health} HP") 
        print(f" {self.p2.name}: {self.p2.health} HP")
        return self

p1 = Pirate('Jack')
p2 = Ninja('Masaru')

game=Game(p1, p2)
game.battle()

















































# class Pirate:
#     def __init__( self , name ):
#         self.name = name
#         self.strength = 15
#         self.speed = 3
#         self.health = 100

#     def show_stats( self ):
#         print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

#     def attack ( self , ninja ):
#         ninja.health -= self.strength
#         return self





# class Ninja:
#     def __init__( self , name ):
#         self.name = name
#         self.strength = 10
#         self.speed = 5
#         self.health = 100
    
#     def show_stats( self ):
#         print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

#     def attack( self , pirate ):
#         pirate.health -= self.strength
#         return self



# michelangelo = Ninja("Michelanglo")
# jack_sparrow = Pirate("Jack Sparrow")
# michelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()
