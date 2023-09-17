# Prevents a user from creating an object of that class
# compels a user overide abstract methods in a child class

# abstract class = a class which contains one or more abstract methods
# abstract method = a method that has a declaration but doesn't have a implementation

import car
import motorcycle
import vehicle

#vehicle = vehicle.Vehicle()
car = car.Car()
motorcycle = motorcycle.Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()

car.stop()
motorcycle.stop()
