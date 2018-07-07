from trip import Trip# remeber to import the trip class here

class Driver:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def my_trips(self):
        return [trip for trip in Trip.all() if trip.driver == self]

    def my_trip_summaries(self):
        return ['{} to {}'.format(trip.start, trip.destination) for trip in self.my_trips()]
