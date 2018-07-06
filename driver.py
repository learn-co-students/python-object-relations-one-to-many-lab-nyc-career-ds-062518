from trip import Trip

class Driver:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def my_trips(self):
        return [trip for trip in Trip.all() if trip._driver.name == self.name]

    def my_trip_summaries(self):
        return [trip._start + ' to ' + trip._destination for trip in self.my_trips()]
