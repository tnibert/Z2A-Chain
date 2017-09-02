import unittest
import main

class maintest(unittest.TestCase):

    def testrandhash(self):
        print(main.generateRandomHash())

    def testcreategenesisblock(self):
        print(main.getGenesisBlock())

if __name__ == '__main__':
    unittest.main()
