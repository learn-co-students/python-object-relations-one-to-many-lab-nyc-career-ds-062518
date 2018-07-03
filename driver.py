from trip import Trip

class Driver:
    def __init__(self, name):
        self.name = name

    def my_trips(self):
        return Trip.my_trips(self)

    def my_trip_summaries(self):
        return Trip.my_trip_summaries(self)
