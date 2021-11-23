class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, Pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.Pet = Pet

    def walk(self):
        self.Pet.play()
        print("Speckler is taking Hodor for a walk.")
        return self

    def feed(self):
        self.Pet.eat()
        print("Speckler has fed Hodor")
        return self

    def bathe(self):
        self.Pet.noise()
        return self

class Pet:
    def __init__(self, name, type, tricks, health=100, energy=100):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25

    def eat(self):
        self.energy +=5
        self.health +=10

    def play(self):
        self.health +=5

    def noise(self):
        print("Ho-Ho-Hodor!")

Hodor = Pet("Hodor", "cat", "scratch")
Speckler = Ninja("Speckler", "Gold", "Hot Cheetos", "pizza", Hodor)

Speckler.walk().feed().bathe()