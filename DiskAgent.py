
# define a specialized agent which knows how to collect
# hard disk usage statistics
#
from getcurrentip import getCurrentIP
from CompLocal import CompLocal

class DiskAgent:

    def __init__(self, masterip, route):
        #Path
        self.masterip = masterip
        self.route = route
        self.hops = 0
        #use the masterip, create a socket, see it's ip.
        self.localip = getCurrentIP(masterip)
        #DON'T KNOW
        self.plusval = 1 
        #Code career    
        #Has to be signed by the server, otherwise wont work.
        self.compLocal = CompLocal()
        self.serverSignature = ""
        
    def dispInfo(self):
        # print out the result
        print "================================="
        print "        Agent Information        "
        print "================================="
        print "free disk space:", self.compLocal.totalfree
        print "local ip is :", self.localip
        print "master ip is:", self.masterip
        print "current hops is:",self.hops
        print "planned route is:", self.route
        print "self plus result is", self.plusval
        print "================================="

    def compute(self):
        import rsa,  cPickle
        from KeyServer import getPublicKey
        from CompLocal import CompLocal
        print "Computation started"
        self.plusval+=1
        print "Plussed"
        #TODO: Verify integrity
        try: 
            dump = cPickle.dumps(self.compLocal, 1)
            _serverPubKey = getPublicKey(self.masterip)
            _serverPubKey.verify(dump, (self.serverSignature,))
            if isinstance(self.compLocal, CompLocal):
                return self.compLocal.compute()
            else:
                return -1

        except rsa.pkcs1.VerificationError as e:
            print "Cannot trust the code, cowardly exiting"
            raise e

        except Exception as e:
            print "Last except excepted: ", str(e)
            raise e
    
    def __eq__(self, other):
        print "comparing"
        return self.__dict__ == other.__dict__
