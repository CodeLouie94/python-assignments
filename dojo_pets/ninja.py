class Ninja():
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        print(f'walks {self.pet.name}')
        return self

    def feed(self):
        print(f'feeds {self.pet.name}')
        return self

    def bathe(self):
        print(f'bathes {self.pet.name}')
        return self

    def check_health(self):
        print(self.pet.health)


