

class Car():

    def __init__(self):
        self.front_left = []
        self.front_right = []
        self.back_left= []
        self.back_right = []

    def add_reading(self, reading):
        if reading.position == "Front left":
            self.front_left.append(reading)
        if reading.position == "Front right":
            self.front_right.append(reading)
        if reading.position == "Back left":
            self.back_left.append(reading)
        if reading.position == "Back right":
            self.back_right.append(reading)

    def latest_readings(self, position):
        if position == "Front left":
            return self.front_left[-1]
        if position == "Front right":
            return self.front_right[-1]
        if position == "Back left":
            return self.back_left[-1]
        if position == "Back right":
            return self.back_right[-1]
