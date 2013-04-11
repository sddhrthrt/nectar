import Crypto 
from Crypto.Cipher import AES
import cPickle
from KeyServer import getPublicKey, getPrivateKey
from DiskAgent import DiskAgent 
from getcurrentip import getCurrentIP

class AgentCareer:
    def __init__(self, agent, nextip=""):
        self.agent = agent
        self.nextip = nextip
    
    def readyToTransport(self):

        if self.nextip == "":
            print "ERROR: No next destination defined, exiting"
            return -1
        #TODO: Encrypt with self's priv key

        ### Encrypt with AES
        PADDING='{'
        BLOCK_SIZE= AES.block_size

        rf = Crypto.Random.new()
        _key = rf.read(BLOCK_SIZE) 
        iv = rf.read(BLOCK_SIZE)
        
        encryptor = AES.new(_key, AES.MODE_CBC, iv)

        ## Pad to make block size okay
        pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
         
        self.agent = iv + encryptor.encrypt(pad(cPickle.dumps(self.agent, -1)))
        
        ### Encrypt the key now 
        _pubkey = getPublicKey(self.nextip)
        self.key = _pubkey.encrypt(_key, b'')[0] 
            
    def unloadAgent(self):

        _privkey = getPrivateKey(self.nextip)
        _key = _privkey.decrypt(self.key)

        PADDING='{'
        encryptor = AES.new(_key, AES.MODE_CBC, self.agent[:16])

        self.agent = cPickle.loads(encryptor.decrypt(self.agent).strip(PADDING)[16:])
         
        if(isinstance(self.agent, DiskAgent)):
            return self.agent
        else:
            print "failed to get agent"
            print "(you are not meant to get this?)"
            return -1
