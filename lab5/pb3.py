class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, make, model, year, mileage):
        super().__init__(make, model, year)
        self.mileage = mileage

    def calculate_mileage(self):
        return f"The {self.make} {self.model} has a mileage of {self.mileage} miles per gallon."

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, mileage):
        super().__init__(make, model, year)
        self.mileage = mileage

    def calculate_mileage(self):
        return f"The {self.make} {self.model} has a mileage of {self.mileage} miles per gallon."

class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def calculate_towing_capacity(self):
        return f"The {self.make} {self.model} has a towing capacity of {self.towing_capacity} pounds."

def main():
    vehicles = [Car("Toyota", "Camry", 2018, 30), Motorcycle("Honda", "CBR", 2019, 40), Truck("Ford", "F-150", 2020, 5000)]
    for vehicle in vehicles:
        if isinstance(vehicle, Car) or isinstance(vehicle, Motorcycle):
            print(vehicle.calculate_mileage())
        if isinstance(vehicle, Truck):
            print(vehicle.calculate_towing_capacity())

if __name__ == "__main__":
    main()