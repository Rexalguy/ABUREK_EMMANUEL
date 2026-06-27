class Vehicle:
    """ Attempting to create a Vehicle class"""

    #Class attribute
    wheels = 4

    
    def __init__(self, make, model, mileage):
        self.make = make
        self.model = model
        self.mileage = mileage

    #Methods
    def drive(self, distance):
        self.mileage += distance
        print(f"Driven {distance} miles. New total: {self.mileage}")

    def display_status(self):
        print(f"Vehicle: {self.make} {self.model} - Mileage: {self.mileage} miles")

    def turn_on(self):
        print(f"The {self.make} {self.model} is turning on.")
        return self

    def honk(self):
        print(f"The {self.make} {self.model} honks: Beep beep!")
        return self

    def brake(self):
        print(f"The {self.make} {self.model} is braking.")
        return self
