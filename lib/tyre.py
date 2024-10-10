from datetime import datetime

class Tyre():

    def __init__(self, position, tread, pressure):
        self.position = position
        self.tread = tread
        self.pressure = pressure
        self.date = datetime.now()
