import car
import motorcycle


car_1 = car.Car()
car_2 = car.Car()
car_3 = car.Car()
bike_1 = motorcycle.Motorcycle()

car.change_color(car_1, "red")
car.change_color(car_2, "white")
car.change_color(car_3, "blue")
car.change_color(bike_1, "black")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)
