from car import Car# import car class here


class Owner:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age


    def find_my_cars(self):
        return [car._make + " " + car._model for car in Car._all if self._name == car._owner._name]
