from ..Vehicle.vehicle import Vehicle ,Car, Bus, Motorcycle
from ..Parking_Spot.parking_spot import Parking_Spot,CarSpot,BusSpot,MotorcycleSpot
from typing import List
import math
from my_logging import MyLogger

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

    def __init__(self, location: tuple, spots: List[Parking_Spot]) -> None:
        self.location = location
        self.spots = spots
        self.motorcycle_spots = []
        self.car_spots = []
        self.bus_spots = []
        self.MyLogger = MyLogger("parking_lot.log", __name__)


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
        
        self.MyLogger.info(f"{vehicle.__class__.__name__} parked at {closest_spot.location}")

        return closest_spot

