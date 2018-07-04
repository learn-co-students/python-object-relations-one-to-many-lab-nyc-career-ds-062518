class Trip:
    _all = []

    def __init__(self, start, destination, driver):
        self._start = start
        self._destination = destination
        self._driver = driver
        Trip._all.append(self)


    #CLASSMETHODS

    @classmethod
    def all(cls):
        return cls._all

    #DECORATORS

    #deocrators for _start

    @property
    def start(self):
       return self._start

    @start.setter
    def start(self, start):
       self._start = start

    #decorators for _destination

    @property
    def destination(self):
       return self._destination

    @destination.setter
    def destination(self, destination):
       self._destination = destination

    #decorators for _driver

    @property
    def driver(self):
       return self._driver

    @driver.setter
    def driver(self, driver):
       self._driver = driver
