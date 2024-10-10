from lib.tyre import *

def test_tyre_inits_with_readings_and_position():
    tyre = Tyre("Front left", "10mm", "500psi")
    actual_position = tyre.position
    expected_position = "Front left"
    assert actual_position == expected_position
    actual_tread = tyre.tread
    expected_tread = "10mm"
    assert actual_tread == expected_tread
    actual_pressure = tyre.pressure
    expected_pressure = "500psi"
    assert actual_pressure == expected_pressure



