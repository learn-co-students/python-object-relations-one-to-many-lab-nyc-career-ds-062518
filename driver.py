# remeber to import the trip class here
from trip import Trip

class Driver:
    def __init__(self, name):
        self.name = name

    def my_trips(self):
        return [trip for trip in Trip._all if trip._driver._name == self._name]

    def my_trip_summaries(self):
        return [trip._start + " to " + trip._destination for trip in Trip._all if trip._driver._name == self._name]

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name
