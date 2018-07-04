# remeber to import the trip class here
from trip import Trip

class Driver:

    _all = []

    def __init__(self, name):
        self.name = name
        Driver._all.append(self)

    #CLASSMETHODS

    @classmethod
    def all(cls):
        return cls._all


    #INSTANCEMETHODS

    def my_trips(self):
        return [trip for trip in Trip.all() if self == trip.driver]

    def my_trip_summaries(self):
        return [trip.start + ' to ' + trip.destination for trip in Trip.all() if self == trip.driver]

    #DECORATORS

    #deocrators for _name

    @property
    def name(self):
       return self._name

    @name.setter
    def name(self, name):
       self._name = name
