from vehicle import Vehicle


car1 = Vehicle("Tesla", "Model S", 30000)
car2 = Vehicle("Honda", "Civic", 50000)



# car1.drive(100)
# car2.drive(50)

# car1.display_status()
# car2.display_status()

# Vehicle.wheels = 3

# car1.wheels = 2

# print(f"Number of wheels on car1: {car1.wheels}")
# print(f"Number of wheels on car2: {car2.wheels}")

car1.turn_on().honk().brake()

