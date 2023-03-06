from my_logging import MyLogger
from math import floor
from ..Vehicle.vehicle import Vehicle, Car, Bus, Motorcycle
from ..Parking_Spot.parking_spot import CarSpot, BusSpot, MotorcycleSpot
from ..Entrance.Entrance import Entrance
from ..ticket.ticket import Ticket


class Parking_Lot:
    def __init__(self, matrix) -> None:
        self.matrix = matrix
        self.MyLogger = MyLogger("parking_lot.log", __name__)

    def Park(self, vehicle: Vehicle, entrance: Entrance):
        self.MyLogger.info(f"Vehicle {vehicle.id} attempting to park")
        
        parking_spot = entrance.get_closest_spot(vehicle)
        if not hasattr(vehicle, "ticket") or vehicle.ticket.deleted:
            vehicle.ticket = Ticket(vehicle.id, parking_spot)
        else:
            vehicle.ticket.parking_space_id = parking_spot
            vehicle.ticket.timer.stop_timer()
        parking_spot.set_occupied()
        self.MyLogger.info(f"Vehicle {vehicle.id} parked at {parking_spot.location}")
        self.MyLogger.info(f"Vehicle {vehicle.brand} parked at {parking_spot.location}")
        self.MyLogger.info(f"Vehicle {vehicle.color} parked at {parking_spot.location}")

        return True , parking_spot.location

    
    def Leave_parking(self, vehicle: Vehicle):
        self.MyLogger.info(f"Vehicle {vehicle.id} attempting to leave")
        fees = vehicle.ticket.fee.calculate_fees(
            vehicle, vehicle.ticket.timer.calculation_time()
        )
        if vehicle.ticket.is_paid:
            space_id = vehicle.ticket.parking_space_id
            space_id.set_occupied()
            vehicle.ticket.start_60_minute()
            self.MyLogger.info(f"Vehicle {vehicle.id} left the parking lot")
        else:
            self.MyLogger.warning(
                f"Vehicle {vehicle.id} has not paid and is attempting to leave"
            )
            print("please pay")
        return True
