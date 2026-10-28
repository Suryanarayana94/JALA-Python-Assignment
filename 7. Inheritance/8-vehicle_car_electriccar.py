# Real-world example: Vehicle -> Car -> ElectricCar
class Vehicle:
    def start_engine(self):
        print("Vehicle engine started")

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

class ElectricCar(Car):
    def start_engine(self):
        print("ElectricCar motor started silently")

for v in (Vehicle(), Car(), ElectricCar()):
    v.start_engine()
