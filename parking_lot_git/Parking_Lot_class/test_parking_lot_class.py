from ..Vehicle.vehicle import Vehicle, Car, Bus, Motorcycle
from ..Parking_Spot.parking_spot import CarSpot, BusSpot, MotorcycleSpot
from ..Entrance.Entrance import Entrance
from ..ticket.ticket import Ticket
from .Parking_lot import Parking_Lot

def test_park_vehicle():
    # Create parking spots
    spots = [
        MotorcycleSpot(1,location=(0, 0)),
        CarSpot(2,location=(0, 1)),
        BusSpot(3,location=(0, 2)),
        MotorcycleSpot(4,location=(1, 0)),
        CarSpot(5,location=(1, 1)),
        BusSpot(6,location=(1, 2)),
    ]
    
    # Create an entrance with the parking spots
    entrance = Entrance(location=(0, 0), spots=spots)
    
    # Create a parking lot with the entrance and the parking spots
    parking_lot = Parking_Lot(matrix=[[entrance, *spots]])

    # Park a motorcycle
    motorcycle = Motorcycle(1,"blue","Toyota")
    success, location = parking_lot.Park(vehicle=motorcycle, entrance=entrance)
    assert success is True
    assert location == (0, 0)

    # Park a car
    car = Car(2,"blue","Toyota")
    success, location = parking_lot.Park(vehicle=car, entrance=entrance)
    assert success is True
    assert location == (0, 1)

    # Park a bus
    bus = Bus(3,"blue","Toyota")
    success, location = parking_lot.Park(vehicle=bus, entrance=entrance)
    assert success is True
    assert location == (0, 2)


def test_leave_parking():
    # Create parking spots
    spots = [
        MotorcycleSpot(1,location=(0, 0)),
        CarSpot(2,location=(0, 1)),
        BusSpot(3,location=(0, 2)),
        MotorcycleSpot(4,location=(1, 0)),
        CarSpot(5,location=(1, 1)),
        BusSpot(6,location=(1, 2)),
    ]
    
    # Create an entrance with the parking spots
    entrance = Entrance(location=(0, 0), spots=spots)
    
    # Create a parking lot with the entrance and the parking spots
    parking_lot = Parking_Lot(matrix=[[entrance, *spots]])

    # Park a motorcycle
    motorcycle = Motorcycle(1,"blue","Toyota")
    success, location = parking_lot.Park(vehicle=motorcycle, entrance=entrance)
    assert success is True

    # Pay and leave the parking lot
    motorcycle.ticket.is_paid = True
    success = parking_lot.Leave_parking(vehicle=motorcycle)
    assert success is True
