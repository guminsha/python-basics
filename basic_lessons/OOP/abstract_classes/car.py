import vehicle


class Car(vehicle.Vehicle):
    def go(self):
        print("You drive the car")

    def stop(self):
        print("This car is stopped")
