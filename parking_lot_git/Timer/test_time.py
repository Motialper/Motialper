import time

import pytest
from timer import ParkingTimer



def test_calculate_time():
    parking_timer = ParkingTimer()
    parking_timer.start_timer()
    time.sleep(2)  # simulate 2 minutes of parking time
    parking_timer.end_timer()
    assert abs(parking_timer.calculation_time() - 2) < 0.1  


def test_calculate_to_days():
    parking_timer = ParkingTimer()
    parking_timer.start_timer()
    time.sleep(0.1)  # simulate 2 days of parking time
    parking_timer.end_timer()
    assert parking_timer.calculation_to_days() == "0 days and 0 minute"


def test_calculate_to_week():
    parking_timer = ParkingTimer()
    parking_timer.start_timer()
    time.sleep(0.1)  # simulate 9 days of parking time
    parking_timer.end_timer()
    assert parking_timer.calculation_to_week() == "0 weeks and 0 days"


def test_calculate_to_months():
    parking_timer = ParkingTimer()
    parking_timer.start_timer()
    time.sleep
    (0.1)  # simulate 40 days of parking time
    parking_timer.end_timer()
    assert parking_timer.calculation_to_months() == "0 months and 0 weeks"

def test_start_timer_to_one_hour():
    parking_timer = ParkingTimer()
    assert parking_timer.start_timer_to_one_hour(0) == True  
    assert parking_timer.start_timer_to_one_hour(-1) == False  
    assert parking_timer.start_timer_to_one_hour(60) == True  
    assert parking_timer.start_timer_to_one_hour(61) == True  
    assert parking_timer.start_timer_to_one_hour(59) == False  
