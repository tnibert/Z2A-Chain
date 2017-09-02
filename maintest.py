import unittest
import Utilities
import BlockChain

class blocktest(unittest.TestCase):

    def testrandhash(self):
        print("\nGenerating random hash")
        print(Utilities.generateRandomHash())

    def testcreategenesisblock(self):
        print("\nTesting genesis block creation")
        print(Utilities.createGenesisBlock())

#    def testcreatesecondblock(self):
#        blockli
#        blocklist.append

class blockchaintest(unittest.TestCase):

    def testblockchainclass(self):
        print("\nCreating one item blockchain")
        mychain = Utilities.BlockChain()
        print(mychain)

    def testgetlatestblock(self):
        print("\nGet latest block")
        mychain = Utilities.BlockChain()
        test = mychain.getLatestBlock()
        print(test)

    def testaddtoblockchain(self):
        print("\nAdding to new block")
        mychain = Utilities.BlockChain()
        mychain.generateNextBlock("Block 2")
        mychain.generateNextBlock("Block 3")
        print(mychain)

if __name__ == '__main__':
    unittest.main()
