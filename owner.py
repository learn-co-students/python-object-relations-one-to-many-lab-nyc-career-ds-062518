from car import Car

class Owner:

    _all = []

    def __init__(self, name, age):
        self._name = name
        self._age = age
        Owner._all.append(self)

    def find_my_cars(self):
        my_ridez = []
        for car in Car.all():
            if not car.owner == self:
                continue
            else:
                # ride = car.make + car.model
                my_ridez.append(car.make + ' ' + car.model)
        return my_ridez

    #CLASSMETHODS

    @classmethod
    def all(cls):
        return cls._all

    #DECORATORS

    #deocrators for _name

    @property
    def name(self):
       return self._name

    @name.setter
    def name(self, name):
       self._name = name

    #decorators for _age

    @property
    def age(self):
       return self._age

    @age.setter
    def age(self, age):
       self._age = age
