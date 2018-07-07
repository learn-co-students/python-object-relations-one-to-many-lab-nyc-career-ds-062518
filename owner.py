from car import Car# import car class here

class Owner:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name (self):
        return self._name
    @property
    def age(self):
        return self._age
    def my_cars(self):
        return [car for car in Car.all() if car.owner==self ]
    def find_my_cars(self):
        return ['{} {}'.format(car.make, car.model) for car in self.my_cars()]
