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
        # trippies = []
        # for going in Trip.all():
        #     if going.driver == self:
        #         trippies.append(going)
        # return trippies
        return [going for going in Trip.all() if going.driver == self]

    def my_trip_summaries(self):
        names_o_trips = []
        for place in self.my_trips():
            names_o_trips.append(str(place.start) + " to " + str(place.destination))
        return names_o_trips
