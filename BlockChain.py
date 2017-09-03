import Utilities
import time

class BlockChain:


    def __init__(self):
        self.blockchain = [Utilities.createGenesisBlock()]

    def getLatestBlock(self):
        return self.blockchain[-1]

    def generateNextBlock(self, blockData):
        previousBlock = self.getLatestBlock()
        nextIndex = previousBlock.index + 1
        nextTimestamp = time.time()
        nextHash = Utilities.calculateHash(nextIndex, previousBlock.currentHash, nextTimestamp, blockData)
        #return Block(nextIndex, previousBlock.currentHash, nextTimestamp, nextHash)
        self.blockchain.append(Block(nextIndex, previousBlock.currentHash, nextTimestamp, blockData, nextHash))

    def __str__(self):
        retstr = ""
        for block in self.blockchain:
            retstr += str(block)
        return retstr

class Block:
    def __init__(self, index, previousHash, timestamp, data, currentHash):
        self.index = index
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.data = data        # we should make this so that it can be non string data
        self.currentHash = currentHash

    def __str__(self):
        return ("\nIndex: " + str(self.index) + "\nTimestamp: " + str(self.timestamp) + "\nData: " + str(self.data) + "\nCurrent Hash: " + str(self.currentHash) + "\nPrevious Hash: " + str(self.previousHash))

    def __eq__(self, other):
        if self.index != other.index:
            return False
        elif self.previousHash != other.previousHash:
            return False
        elif self.timestamp != other.timestamp:
            return False
        elif self.data != other.data:
            return False
        elif self.currentHash != other.currentHash:
            return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)
