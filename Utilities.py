#! /usr/bin/env python
import hashlib
import time
import random

from BlockChain import Block, BlockChain

"""
So here's an idea: make the data on a given block only available to author, probably using public/private key encryption
"""

# used locally

def generateRandomHash():
    return ("%032x" % random.getrandbits(256))

def createGenesisBlock():
    # customize hash
    return Block(0, '0', time.time(), "Genesis Block", generateRandomHash()) #'0q23nfa0se8fhPH234hnjldapjfasdfansdf23')

def calculateHash(index, previousHash, timestamp, data):
    # make data calculated based on bits
    value = str(index) + str(previousHash) + str(timestamp) + str(data)
    sha = hashlib.sha256(value.encode('utf-8'))
    return str(sha.hexdigest())

def calculateHashForBlock(block):
    return calculateHash(block.index, block.previousHash, block.timestamp, block.data)


# check if two blocks are the same
# we can move this into a method of the block class - MOVED
def isSameBlock(block1, block2):
    return block1 == block2


# these two can be moved into BlockChain classes
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
