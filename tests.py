import unittest
import cPickle, md5, rsa
from DiskAgent import *
from AgentCareer import *
from MaliciousAgent import *
from testfixtures import Comparison as C

class TestAgentFunctionality(unittest.TestCase):

    def setUp(self):
        self.agent = DiskAgent('127.0.0.1', [])
        #### Sign the agent
        binstr = cPickle.dumps(self.agent.compLocal, 1)
        _privkey = getPrivateKey(self.agent.masterip)
        _pubkey = getPublicKey(self.agent.masterip)
        self.agent.serverSignature = _privkey.sign(binstr, b'')[0]

    def test_compLocal(self):
        self.assertGreater(self.agent.compute(), 0)

class TestAgentSecurity(unittest.TestCase):

    def setUp(self):
        self.agent = DiskAgent('127.0.0.1', [])
        #### Sign the agent
        binstr = cPickle.dumps(self.agent.compLocal, 1)
        _privkey = getPrivateKey(self.agent.masterip)
        _pubkey = getPublicKey(self.agent.masterip)
        self.agent.serverSignature = _privkey.sign(binstr, b'')[0]
    
    def test_execution(self):
        self.assertGreater(self.agent.compute(), 0)

    def test_security_on_code_change(self):
        newagent = MaliciousAgent('127.0.0.51', [])
        self.agent.compLocal = newagent.compLocal
        self.assertEqual(self.agent.compute(), -1)
   
class TestAgentCareer(unittest.TestCase):

    def setUp(self):
        self.agent = DiskAgent("127.0.0.1", ["127.0.0.1", "127.0.0.1"])
        #### Sign the agent
        binstr = cPickle.dumps(self.agent.compLocal, 1)
        _privkey = getPrivateKey(self.agent.masterip)
        _pubkey = getPublicKey(self.agent.masterip)
        self.agent.serverSignature = _privkey.sign(binstr, b'')[0]
    
    def test_packaging(self):
        career = AgentCareer(self.agent, "127.0.0.1")
        career.readyToTransport()
        agent = career.unloadAgent()
        self.maxDiff= None
        self.assertEqual(agent.__dict__, self.agent.__dict__)
