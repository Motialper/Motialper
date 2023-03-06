
class Vehicle:

    def __init__(self, id, color, brand) -> None:
         
        self.id = id
        self.color = color
        self.brand = brand
    


class Car(Vehicle):

    def __init__(self, id, color, brand) -> None:
        super().__init__(id, color, brand)


class Motorcycle(Vehicle):

    def __init__(self, id, color, brand) -> None:
        super().__init__(id, color, brand)


class Bus(Vehicle):

    def __init__(self, id, color, brand) -> None:
        super().__init__(id, color, brand)

class Parking_Spot:
    """
    A class to represent a parking spot.

    Attributes:
        id (int): The unique identifier of the parking spot.
        location (str): The location of the parking spot.
        occupied (bool): The occupancy status of the parking spot.

    Methods:
        get_id() -> int: Returns the unique identifier of the parking spot.
        get_location() -> str: Returns the location of the parking spot.
        get_occupied() -> bool: Returns the occupancy status of the parking spot.
        get_info() -> None: Prints the parking spot's id, location, and occupancy status.
        set_id(new_id: int) -> None: Sets the unique identifier of the parking spot.
        set_location(new_location: tuple) -> None: Sets the location of the parking spot.
        set_occupied() -> None: Sets the occupancy status of the parking spot to True.
    """
    def __init__(self, id: int, location: tuple) -> None:
        self.id = id
        self.location = location
        self.occupied = False

    def get_id(self) -> int:
        """Returns the unique identifier of the parking spot."""
        return self.id 
    
    def get_location(self) -> tuple:
        """Returns the location of the parking spot."""
        return self.location 

    def get_occupied(self) -> bool:
        """Returns the occupancy status of the parking spot."""
        return self.occupied 
    
    def get_info(self) -> None:
        """Prints the parking spot's id, location, and occupancy status."""
        print(f"The ID is {self.id}, The location is {self.location}, To say that the spot is occupied is {self.occupied}")

    def set_id(self, new_id: int) -> None:
        """Sets the unique identifier of the parking spot."""
        self.id = new_id

    def set_location(self, new_location: tuple) -> None:
        """Sets the location of the parking spot."""
        self.location = new_location

    def set_occupied(self) -> None:
        """Sets the occupancy status of the parking spot to True."""
        self.occupied = True
###########################################################################################
#from Parking_Spot import Parking_Spot

class MotorcycleSpot(Parking_Spot):
    def __init__(self, id: int, location: tuple, occupied: bool = False) -> None:
        """
        A class representing a motorcycle parking spot.

        Args:
            id (int): The ID of the parking spot.
            location (str): The location of the parking spot.
            occupied (bool, optional): Whether or not the parking spot is occupied. Defaults to False.
        """
        super().__init__(id, location)

class CarSpot(Parking_Spot):
    def __init__(self, id: int, location: tuple, occupied: bool = False) -> None:
        """
        A class representing a car parking spot.

        Args:
            id (int): The ID of the parking spot.
            location (str): The location of the parking spot.
            occupied (bool, optional): Whether or not the parking spot is occupied. Defaults to False.
        """
        super().__init__(id, location)

class BusSpot(Parking_Spot):
    def __init__(self, id: int, location: tuple, occupied: bool = False) -> None:
        """
        A class representing a bus parking spot.

        Args:
            id (int): The ID of the parking spot.
            location (str): The location of the parking spot.
            occupied (bool, optional): Whether or not the parking spot is occupied. Defaults to False.
        """
        super().__init__(id, location)

from typing import List
import math

class Entrance:
    """
    A class representing an entrance to a parking lot.

    Attributes:
        location (str): The location of the entrance.
        spots (List[Parking_Spot]): The list of parking spots at the entrance.
        rows (int): The number of rows in the parking lot.
        num_cols (int): The number of columns in the parking lot.
        motorcycle_spots (List[Parking_Spot]): The list of motorcycle parking spots at the entrance.
        car_spots (List[Parking_Spot]): The list of car parking spots at the entrance.
        bus_spots (List[Parking_Spot]): The list of bus parking spots at the entrance.

    Methods:
        get_closest_spot(vehicle: Vehicle) -> Parking_Spot: Returns the closest unoccupied parking spot for a given vehicle.
    """

    def __init__(self, location: tuple, spots: List[Parking_Spot], rows: int, num_cols: int) -> None:
        self.location = location
        self.spots = spots
        self.rows = rows
        self.num_cols = num_cols
        self.motorcycle_spots = []
        self.car_spots = []
        self.bus_spots = []

        for spot in spots:
            if isinstance(spot, MotorcycleSpot):
                self.motorcycle_spots.append(spot)
            elif isinstance(spot, CarSpot):
                self.car_spots.append(spot)
            elif isinstance(spot, BusSpot):
                self.bus_spots.append(spot)

        self.motorcycle_spots = sorted(self.motorcycle_spots, key=lambda spot: spot.location[1])
        self.car_spots = sorted(self.car_spots, key=lambda spot: spot.location[1])
        self.bus_spots = sorted(self.bus_spots, key=lambda spot: spot.location[1])

    def get_closest_spot(self, vehicle: Vehicle) -> Parking_Spot:
        if isinstance(vehicle, Motorcycle):
            spots = self.motorcycle_spots
        elif isinstance(vehicle, Car):
            spots = self.car_spots
        elif isinstance(vehicle, Bus):
            spots = self.bus_spots
        else:
            raise ValueError("Invalid vehicle type")

        closest_spot = None
        closest_distance = math.inf
        for spot in spots:
            if not spot.get_occupied():
                distance = math.sqrt((spot.location[0])**2 + (spot.location[1])**2)
                if distance < closest_distance:
                    closest_spot = spot
                    closest_distance = distance

        if closest_spot is None:
            raise ValueError("No available parking spots")

        return closest_spot


import math
def test_parking_lot():
   

    # Create parking spots
    motorcycle_spot_1 = MotorcycleSpot(1, (2,7))
    car_spot_1 = CarSpot(2, (1,1))
    car_spot_2 = CarSpot(3, (2,1))
    bus_spot_1 = BusSpot(4, (1,2))
    bus_spot_2 = BusSpot(5, (3,1))

    # Create entrance and add parking spots
    entrance = Entrance((4,6), [motorcycle_spot_1, car_spot_1, car_spot_2, bus_spot_1, bus_spot_2], 2, 3)

    # Test get_closest_spot method for motorcycle
    motorcycle = Motorcycle(1, "red", "Harley Davidson")
    closest_spot = entrance.get_closest_spot(motorcycle)
    assert closest_spot == motorcycle_spot_1

    # Test get_closest_spot method for car
    car = Car(2, "blue", "Toyota")
    closest_spot = entrance.get_closest_spot(car)
    assert closest_spot == car_spot_1

    # Test get_closest_spot method for bus
    bus = Bus(3, "yellow", "Volvo")
    closest_spot = entrance.get_closest_spot(bus)
    assert closest_spot == bus_spot_1
