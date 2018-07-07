import os


class Creature(object):
    def __init__(self, name):
        self.name = name

    def name_upper(self):
        return str.upper(self.name)

if __name__ == '__main__':
    c = Creature('dog')
    print(c.name_upper())