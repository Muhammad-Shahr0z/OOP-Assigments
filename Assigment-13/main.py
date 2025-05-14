# 13. Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.


class Engine:
    def start(self):
        print("Engine Stated")




class Car:
    def __init__(self):
        self.engine = Engine() #composition
        
    def car_start(self):
        self.engine.start()
        print("Car Started")



car:Car = Car()
car.car_start()



        
    

