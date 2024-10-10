from lib.car_multi_class import *

def test_car_inits_with_all_lists_empty():
    car = Car()
    actual = car.front_left
    expected = []
    assert actual == expected