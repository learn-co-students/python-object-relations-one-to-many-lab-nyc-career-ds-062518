class Car:
    _all = []

    @classmethod
    def all(cls):
        return cls._all

    def __init__(self, make, model, year, owner):
        self._make = make
        self._model = model
        self._year = year
        self._owner = owner

        Car.all().append(self)

    @property
    def owner(self):
        return self._owner
    @property
    def make(self):
        return self._make
    @property
    def model(self):
        return self._model
    @property
    def year(self):
        return self._year
