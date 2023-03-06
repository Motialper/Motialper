from .fees import Fees
from ..Vehicle.vehicle import Vehicle ,Car, Bus, Motorcycle
import pytest

def test_calculate_fees():
    fees1 = Fees()
    fees2 = Fees()
    fees3 = Fees()
    assert fees1.calculate_fees(Motorcycle(1,"blue","toyota") ,2) == 40
    assert fees2.calculate_fees(Car(2,"blue","toyota"), 5) == 120
    assert fees3.calculate_fees(Bus(3,"blue","toyota"), 5) == 140
