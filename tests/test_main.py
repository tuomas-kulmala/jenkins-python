import unittest

from src.main import Creature


class MainTest(unittest.TestCase):
    def testUpperName(self):
        creature = Creature('test')
        self.assertEqual(creature.name_upper(),str.upper('test'))

if __name__ == '__main__':
    unittest.main()