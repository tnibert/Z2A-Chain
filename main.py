#! /usr/bin/env python
import hashlib

class Block:
    def __init__(self, index, previousHash, timestamp, data, currentHash):
        self.index = index
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.data = data
        self.currentHash = currentHash

def getGenesisBlock():
    # change timestamp to current time
    # customize hash
    return Block(0, '0', '1496518102.896031', "My very first block :)", '0q23nfa0se8fhPH234hnjldapjfasdfansdf23')

blockchain = [getGenesisBlock()]

def calculateHash(index, previousHash, timestamp, data):
    value = str(index) + str(previousHash) + str(timestamp) + str(data)
    sha = hashlib.sha256(value.encode('utf-8'))
    return str(sha.hexdigest())

def calculateHashForBlock(block):
    return calculateHash(block.index, block.previousHash, block.timestamp, block.data)

