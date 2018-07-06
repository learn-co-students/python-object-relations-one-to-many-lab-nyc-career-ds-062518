class Trip:
    _all = []

    def __init__(self, start, destination, driver):
        self._start = start
        self._destination = destination
        self._driver = driver
        Trip._all.append(self)

    @property
    def start(self):
        return self._start

    @property
    def destination(self):
        return self._destination

    @property
    def driver(self):
        return self._driver

    @classmethod
    def all(cls):
        return cls._all
