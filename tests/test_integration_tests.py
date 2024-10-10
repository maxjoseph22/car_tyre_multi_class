from lib.car_multi_class import *
from lib.tyre import *

def test_add_reading_to_tyre():
    car = Car()
    reading = Tyre("Front left", "10mm", "500psi")
    car.add_reading(reading)
    assert car.front_left == [reading]

def test_add_reading_to_tyre_bl():
    car = Car()
    reading = Tyre("Back left", "10mm", "500psi")
    car.add_reading(reading)
    assert car.back_left == [reading]

def test_latest_reading():
    car = Car()
    reading_1 = Tyre("Back left", "10mm", "500psi")
    car.add_reading(reading_1)
    reading_2 = Tyre("Back left", "5mm", "300psi")
    car.add_reading(reading_2)
    assert car.latest_readings("Back left") == reading_2

def test_latest_reading_again():
    car = Car()
    reading_1 = Tyre("Back left", "10mm", "500psi")
    car.add_reading(reading_1)
    reading_2 = Tyre("Back left", "5mm", "300psi")
    car.add_reading(reading_2)
    reading_3 = Tyre("Back left", "2mm", "304psi")
    car.add_reading(reading_3)
    assert car.latest_readings("Back left") == reading_3

