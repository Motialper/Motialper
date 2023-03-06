from math import floor
from my_logging import MyLogger
from ..Vehicle.vehicle import Vehicle ,Car, Bus, Motorcycle

class Fees:
    """
    A class for calculating parking fees based on the type of vehicle and duration of parking.

    Attributes:
        fee_for_3_first_hours (int): the fee for the first 3 hours of parking.
        fee_for_24_hours (int): the fee for every 24 hours of parking.
        motorcycle_fee (int): the fee for parking a motorcycle.
        car_fee (int): the fee for parking a car.
        bus_fee (int): the fee for parking a bus.
        paid (int): the amount that has already been paid for parking.
    Methods:
        calculate_fees: Calculates the parking fee based on the type of vehicle and duration of parking.
    """
    fee_for_3_first_hours = 20
    fee_for_24_hours = 100
    motorcycle_fee = 20
    car_fee = 30
    bus_fee = 40

    def __init__(self):
        self.paid = 0
        self.MyLogger = MyLogger("parking_lot.log", __name__)


    def calculate_fees(self, vehicle: Vehicle, hours: int) -> int:
        """
        Calculates the parking fee based on the type of vehicle and duration of parking.

        Args:
        vehicle_type (VehicleType): the type of the vehicle being parked.
        hours (int): the duration of the parking in hours.

        Returns:
        int: the total parking fee.
        """
        self.MyLogger.info(f"Vehicle type: {type(vehicle).__name__}, Hours: {hours}, Total fee: {self.paid}")
        if isinstance(vehicle, Motorcycle):
            fee_per_hour = self.motorcycle_fee
        elif isinstance(vehicle, Car):
            fee_per_hour = self.car_fee
        elif isinstance(vehicle, Bus):
            fee_per_hour = self.bus_fee
        else:
            raise ValueError("Invalid vehicle type")
        
        whole_days = floor(hours / 24)
        first_hours_fee = 0
        if hours < 3:
            first_hours_fee = hours * self.fee_for_3_first_hours - self.paid 
            self.paid += first_hours_fee 
            return first_hours_fee
        else:
            first_hours_fee = 3 * self.fee_for_3_first_hours
            hours -= 3

            fee = (whole_days * self.fee_for_24_hours + first_hours_fee + fee_per_hour * hours) - self.paid
            return fee

            
    @classmethod
    def get_fee_for_3_first_hours(cls):
        return cls.fee_for_3_first_hours 
    @classmethod
    def get_fee_for_24_hours(cls):
        return cls.fee_for_24_hours

    @classmethod
    def get_motorcycle_fee(cls) -> int:
        return cls.motorcycle_fee
    
    @classmethod
    def get_car_fee(cls):
       return cls.car_fee 

    @classmethod
    def get_bus_fee(cls):
       return cls.bus_fee
