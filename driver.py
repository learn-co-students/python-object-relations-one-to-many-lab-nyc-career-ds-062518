# remeber to import the trip class here
from trip import Trip

class Driver:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name

    def my_trips(self):
        return Trip.my_trips(self)

    def my_trip_summaries(self):
        return Trip.my_trip_summaries(self)
