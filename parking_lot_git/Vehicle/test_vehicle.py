# test_vehicle.py

from vehicle import car, motorcycle, bus

def test_car():
    c = car("1234", "red", "Toyota")
    assert c.id == "1234"
    assert c.color == "red"
    assert c.brand == "Toyota"

def test_motorcycle():
    m = motorcycle("5678", "blue", "Honda")
    assert m.id == "5678"
    assert m.color == "blue"
    assert m.brand == "Honda"

def test_bus():
    b = bus("91011", "green", "Mercedes-Benz")
    assert b.id == "91011"
    assert b.color == "green"
    assert b.brand == "Mercedes-Benz"
    
