import BlockChain
import Utilities

# build off https://benediktkr.github.io/dev/2016/02/04/p2p-with-twisted.html

# generate uuid for each network node
from uuid import uuid4
generate_nodeid = lambda: str(uuid4())

from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor

import json


class MyProtocol(Protocol):
    def __init__(self, factory):
        self.factory = factory
        self.state = "HELLO"
        self.remote_nodeid = None
        self.nodeid = self.factory.nodeid

    def connectionMade(self):
        print("Connection from", self.transport.getPeer())

        def connectionLost(self, reason):
            if self.remote_nodeid in self.factory.peers:
                self.factory.peers.pop(self.remote_nodeid)

        print(self.nodeid, "disconnected")

    def dataReceived(self, data):
        for line in data.splitlines():
            line = line.strip()
            if self.state == "HELLO":
                self.handle_hello(line)
                self.state = "READY"

    def send_hello(self):
        hello = json.puts({'nodeid': self.nodeid, 'msgtype': 'hello'})
        self.transport.write(hello + "\n")

    def handle_hello(self, hello):
        hello = json.loads(hello)
        self.remote_nodeid = hello["nodeid"]
        if self.remote_nodeid == self.nodeid:
            print("Connected to myself.")
            self.transport.loseConnection()
        else:
            self.factory.peers[self.remote_nodeid] = self


class MyFactory(Factory):
    def startFactory(self):
        self.peers = {}
        self.nodeid = generate_nodeid()

    def buildProtocol(self, addr):
        return NCProtocol(self)


endpoint = TCP4ServerEndpoint(reactor, 5999)
endpoint.listen(MyFactory())