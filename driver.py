from trip import Trip

class Driver:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def my_trips(self):
        return [trip for trip in Trip._all if trip.driver == self]

    def my_trip_summaries(self):
        return [trip.start + " to " + trip.destination for trip in self.my_trips()]
