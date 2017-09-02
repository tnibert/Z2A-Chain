import unittest
import main

class maintest(unittest.TestCase):

    def testrandhash(self):
        print(main.generateRandomHash())

if __name__ == '__main__':
    unittest.main()
