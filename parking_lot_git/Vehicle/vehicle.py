#from my_logging import MyLogger


class Vehicle:

    def __init__(self, id, color, brand) -> None:
         
        self.id = id
        self.color = color
        self.brand = brand
        #self.MyLogging = MyLogger("parking_lot.log", __name__)
    

class Car(Vehicle):

    def __init__(self, id, color, brand) -> None:
        super().__init__(id, color, brand)
        
class Motorcycle(Vehicle):

    def __init__(self, id, color, brand) -> None:
        super().__init__(id, color, brand)


class Bus(Vehicle):

    def __init__(self, id, color, brand) -> None:
        super().__init__(id, color, brand)
