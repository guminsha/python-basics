# super() = Function used to give access to the methods of parent class
#          Returns a temporary object of a parent class when used
import square
import cube

square = square.Square(3, 3)
cube = cube.Cube(3, 3, 3)

print(square.area())
print(cube.volume())
