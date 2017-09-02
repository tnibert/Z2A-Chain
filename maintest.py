import unittest
import main

class blocktest(unittest.TestCase):

    def testrandhash(self):
        print("Generating random hash")
        print(main.generateRandomHash())

    def testcreategenesisblock(self):
        print("Testing genesis block creation")
        print(main.createGenesisBlock())

#    def testcreatesecondblock(self):
#        blockli
#        blocklist.append

class blockchaintest(unittest.TestCase):

    def testblockchainclass(self):
        print("Creating one item blockchain")
        mychain = main.BlockChain()
        print(mychain)

    def testgetlatestblock(self):
        print("Get latest block")
        mychain = main.BlockChain()
        test = mychain.getLatestBlock()
        print(test)

    def testaddtoblockchain(self):
        print("Adding to new block")
        mychain = main.BlockChain()
        mychain.generateNextBlock("Block 2")
        mychain.generateNextBlock("Block 3")
        print(mychain)

if __name__ == '__main__':
    unittest.main()
