from ..fees.fees import Fees
from ..Entrance.Entrance import Entrance
from ..Parking_Lot_class.Parking_lot import Parking_Lot

class Admin1:
    """
    A class representing an admin user of the parking system.

    Attributes:
        username (str): the username of the admin user.
        password (str): the password of the admin user.
    Methods:
        add_door: Adds a door to a parking lot.
        login: Verifies the login credentials of the admin user.
        modify_fee_for_3_first_hours: Modifies the fee for the first 3 hours of parking.
        modify_fee_for_24_hours: Modifies the fee for every 24 hours of parking.
        modify_motorcycle_fee: Modifies the fee for parking a motorcycle.
        modify_car_fee: Modifies the fee for parking a car.
        modify_bus_fee: Modifies the fee for parking a bus.
    """
    def __init__(self, username: str, password: str):
        """
        Initializes an instance of the Admin1 class.

        Args:
        username (str): the username of the admin user.
        password (str): the password of the admin user.
        """
        self.username = username
        self.password = password

    def add_entrance(self, location: tuple, parking_lot: Parking_Lot):
        """
        Adds an entrance to a parking lot.

        Args:
            location (tuple): the location of the entrance as a tuple of row and column.
            parking_lot (Parking_Lot): the parking lot to add the entrance to.
        """
        entrance = Entrance(location, parking_lot.matrix)
        row, column = location
        parking_lot.matrix[row][column] = entrance

    def login(self, username: str, password: str) -> bool:
        """
        Verifies the login credentials of the admin user.

        Args:
        username (str): the username to verify.
        password (str): the password to verify.

        Returns:
        bool: True if the credentials are valid, False otherwise.
        """
        return username == self.username and password == self.password

    @classmethod
    def modify_fee_for_3_first_hours(cls, new_fee: int):
        Fees.fee_for_3_first_hours = new_fee

    @classmethod
    def modify_fee_for_24_hours(cls, new_fee: int):
        Fees.fee_for_24_hours = new_fee

    @classmethod
    def modify_motorcycle_fee(cls, new_fee: int):
        Fees.motorcycle_fee = new_fee

    @classmethod
    def modify_car_fee(cls, new_fee: int):
        Fees.car_fee = new_fee

    @classmethod
    def modify_bus_fee(cls, new_fee: int):
        Fees.bus_fee = new_fee


    