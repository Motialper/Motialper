from ..fees.fees import Fees
from ..Entrance.Entrance import Entrance
from ..Parking_Lot_class.Parking_lot import Parking_Lot
from .Parking_admin import Admin1



def test_add_entrance():
    # Initialize a Parking_Lot object
    matrix = [[None for i in range(10)] for j in range(10)]
    parking_lot = Parking_Lot(matrix)

    # Initialize an Admin1 object
    admin = Admin1("admin", "password")

    # Add an entrance to the parking lot using the admin user
    admin.add_entrance((0, 0), parking_lot)

    # Verify that the entrance has been added to the parking lot
    assert isinstance(parking_lot.matrix[0][0], Entrance)





def test_modify_motorcycle_fee():

    # Modify motorcycle fee using classmethod
    Admin1.modify_motorcycle_fee(25)

    # Check if motorcycle fee has been modified
    assert Fees.get_motorcycle_fee() == 25

    Admin1.modify_car_fee(25)
    assert Fees.get_car_fee() == 25