class Animal:
    def __init__(self, name, age, habitat):
        self.name = name
        self.age = age
        self.habitat = habitat

    def eat(self):
        print("The animal is eating.")

    def sleep(self):
        print("The animal is sleeping.")

class Mammal(Animal):
    def __init__(self, name, age, habitat, fur_color):
        super().__init__(name, age, habitat)
        self.fur_color = fur_color

    def give_birth(self):
        print("The mammal is giving birth.")

class Bird(Animal):
    def __init__(self, name, age, habitat, wingspan):
        super().__init__(name, age, habitat)
        self.wingspan = wingspan

    def fly(self):
        print("The bird is flying.")

class Fish(Animal):
    def __init__(self, name, age, habitat, water_type):
        super().__init__(name, age, habitat)
        self.water_type = water_type

    def swim(self):
        print("The fish is swimming.")

def main():
    animals = [Mammal("Dog", 5, "Land", "Brown"), Bird("Eagle", 10, "Air", 2), Fish("Shark", 15, "Water", "Saltwater")]
    for animal in animals:
        animal.eat()
        animal.sleep()
        if isinstance(animal, Mammal):
            animal.give_birth()
        if isinstance(animal, Bird):
            animal.fly()
        if isinstance(animal, Fish):
            animal.swim()

if __name__ == "__main__":
    main()
