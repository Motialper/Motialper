from enum import Enum
from ..fees.fees import Fees
from ..Timer.timer import ParkingTimer


class Ticket:
    def __init__(self, vehicle_id, parking_space_id):
        self.vehicle_id = vehicle_id
        self.parking_space_id = parking_space_id
        self.timer = ParkingTimer()
        self.fee = Fees()
        self.is_paid = True
        self.deleted = False


    def get_car_id(self):
        return self.vehicle_id

    def get_parking_space(self):
        return self.parking_space_id

    def get_time_obj(self):
        return self.timer

    def get_fee_obj(self):
        return self.fee

    def Change_is_paid(self,status):
        self.is_paid = status

    def free_ticket(self):
        self.deleted = True

    def start_60_minute(self):
        if self.timer.start_timer_to_one_hour() == True :
            self.free_ticket()

