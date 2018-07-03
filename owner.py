from car import Car


class Owner:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age

    def find_my_cars(self):
        return [car.make + ' ' + car.model for car in Car.all() if car.owner == self]
