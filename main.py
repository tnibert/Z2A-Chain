# to start we'll follow this tutorial: http://blockxchain.org/2017/06/04/building-a-blockchain-with-python-1/
#! /usr/bin/env python
import hashlib
import time
import random

class Block:
    def __init__(self, index, previousHash, timestamp, data, currentHash):
        self.index = index
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.data = data        # we should make this so that it can be non string data
        self.currentHash = currentHash

    def __str__(self):
        return ("Index: " + str(self.index) + "\nTimestamp: " + str(self.timestamp) + "\nData: " + str(self.data) + "\nCurrent Hash: " + str(self.currentHash) + "\nPrevious Hash: " + str(self.previousHash))

def generateRandomHash():
    return ("%032x" % random.getrandbits(256))

def getGenesisBlock():
    # change timestamp to current time
    # customize hash
    return Block(0, '0', time.time(), "Genesis Block", generateRandomHash()) #'0q23nfa0se8fhPH234hnjldapjfasdfansdf23')

blockchain = [getGenesisBlock()]

def calculateHash(index, previousHash, timestamp, data):
    # make data calculated based on bits
    value = str(index) + str(previousHash) + str(timestamp) + str(data)
    sha = hashlib.sha256(value.encode('utf-8'))
    return str(sha.hexdigest())

def calculateHashForBlock(block):
    return calculateHash(block.index, block.previousHash, block.timestamp, block.data)

def getLatestBlock():
    return blockchain[len(blockchain)-1]

def generateNextBlock(blockData):
    previousBlock = getLatestBlock()
    nextIndex = previousBlock.index + 1
    nextTimestamp = time.time()
    nextHash = calculateHash(nextIndex, previousBlock.currentHash, nextTimestamp, blockData)
    return Block(nextIndex, previousBlock.currentHash, nextTimestamp, nextHash)

# check if two blocks are the same
# we can move this into a method of the block class
def isSameBlock(block1, block2):
    if block1.index != block2.index:
        return False
    elif block1.previousHash != block2.previousHash:
        return False
    elif block1.timestamp != block2.timestamp:
        return False
    elif block1.data != block2.data:
        return False
    elif block1.currentHash != block2.currentHash:
        return False
    return True

# determine if new block is valid
def isValidNewBlock(newBlock, previousBlock):
    if previousBlock.index + 1 != newBlock.index:
        print('Indices Do Not Match Up')
        return False
    elif previousBlock.currentHash != newBlock.previousHash:
        print("Previous hash does not match")
        return False
    elif calculateHashForBlock(newBlock) != newBlock.hash:
        print("Hash is invalid")
        return False
    return True

# iterate over entire list to check chain
def isValidChain(bcToValidate):
    if not isSameBlock(bcToValidate[0], getGenesisBlock()):
        print('Genesis Block Incorrect')
        return False

    tempBlocks = [bcToValidate[0]]
    for i in range(1, len(bcToValidate)):
        if isValidNewBlock(bcToValidate[i], tempBlocks[i-1]):
            tempBlocks.append(bcToValidate[i])
        else:
            return False
    return True

# next: incorporate into consensus network
