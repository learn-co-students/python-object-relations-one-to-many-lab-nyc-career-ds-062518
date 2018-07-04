class Car:

    _all = []

    def __init__(self, make, model, year, owner):
        self._make = make
        self._model = model
        self._year = year
        self._owner = owner
        Car._all.append(self)

    #CLASSMETHODS

    @classmethod
    def all(cls):
        return cls._all

    #DECORATORS

    #deocrators for _make

    @property
    def make(self):
       return self._make

    @make.setter
    def make(self, make):
       self._make = make

    #decorators for _model

    @property
    def model(self):
       return self._model

    @model.setter
    def model(self, model):
       self._model = model

    #decorators for _year

    @property
    def year(self):
       return self._year

    @year.setter
    def year(self, year):
       self._year = year

    #decorators for _owner

    @property
    def owner(self):
       return self._owner

    @owner.setter
    def owner(self, owner):
       self._owner = owner
