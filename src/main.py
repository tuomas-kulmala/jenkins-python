import os
from future.types import bytes, dict, int, range, str

class Creature(object):
    def __init__(self, name: str):
        self.name = name

    def name_upper(self):
        return str.upper(self.name)


if __name__ == '__main__':
    c = Creature('dog')
    print(c.name_upper())
    print(c.add(1))