from DiskAgent import * 
import cPickle
import rsa

#### create new agent
#agentx = DiskAgent(masterip,groute)
agentx = DiskAgent(0, [])
#### Sign the agent
binstr = cPickle.dumps(agentx.compLocal, 1)
(pub, priv) = rsa.newkeys(512)
agentx.serverSignature = rsa.sign(binstr, priv, 'MD5')
agentx.serverPubKey = pub
agentx.compute()
