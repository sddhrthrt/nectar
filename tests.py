import unittest
import cPickle, md5, rsa
from DiskAgent import *
from AgentCareer import *
from testfixtures import Comparison as C

class TestAgentFunctionality(unittest.TestCase):

    def setUp(self):
        self.agent = DiskAgent(0, [])
        #### Sign the agent
        binstr = cPickle.dumps(self.agent.compLocal, 1)
        (pub, priv) = rsa.newkeys(512)
        self.agent.serverSignature = rsa.sign(binstr, priv, 'MD5')
        self.agent.serverPubKey = pub

    def test_compLocal(self):
        self.assertGreater(self.agent.compute(), 0)

class TestAgentSecurity(unittest.TestCase):

    def setUp(self):
        self.agent = DiskAgent(0, [])
        #### Sign the agent
        binstr = cPickle.dumps(self.agent.compLocal, 1)
        (pub, priv) = rsa.newkeys(512)
        self.agent.serverSignature = rsa.sign(binstr, priv, 'MD5')
        self.agent.serverPubKey = pub
    
    def test_execution(self):
        self.assertGreater(self.agent.compute(), 0)

    def test_security_on_code_change(self):
        with self.assertRaises(rsa.pkcs1.VerificationError):
            self.agent.compLocal = {}
            self.agent.compute()
   
class TestAgentCareer(unittest.TestCase):

    def setUp(self):
        self.agent = DiskAgent("127.0.0.1", ["127.0.0.1", "127.0.0.1"])
        #### Sign the agent
        binstr = cPickle.dumps(self.agent.compLocal, 1)
        #TODO: Use GetPublicKey
        (pub, priv) = rsa.newkeys(512)
        self.agent.serverSignature = rsa.sign(binstr, priv, 'MD5')
        self.agent.serverPubKey = pub
    
    #def test_packaging(self):
        #career = AgentCareer(self.agent, "127.0.0.1")
        #career.readyToTransport()
        #agent = career.unloadAgent()
        #self.assertEqual(C(agent), self.agent)
