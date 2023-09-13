from car import Car

car_1 = Car("Chevy", "Corvette", 2021, "Blue")
car_2 = Car("Ford", "Mustang", 2022, "Red")

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

#car_2.drive()
#car_1.stop()

Car.wheels = 2

print(car_1.wheels)
print(car_2.wheels)
