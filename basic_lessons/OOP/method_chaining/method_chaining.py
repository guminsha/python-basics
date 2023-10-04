# method chaining = Calling multiple methodes sequentially
#                   each call performs an action on the same object and returns self

import car

car = car.Car()

# car.turn_on()
# car.drive()

car.turn_on().drive()

(car.turn_on()
 .drive()
 .brake()
 .turn_off())
