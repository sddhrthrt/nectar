
# define a specialized agent which knows how to collect
# hard disk usage statistics
#
from getcurrentip import getCurrentIP
from BadCompLocal import CompLocal

class MaliciousAgent:

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
        print "\t ================================="
        print "\t         Agent Information        "
        print "\t ================================="
        print "\t free disk space:", self.compLocal.totalfree
        print "\t local ip is :", self.localip
        print "\t master ip is:", self.masterip
        print "\t current hops is:",self.hops
        print "\t planned route is:", self.route
        print "\t self plus result is", self.plusval
        print "\t ================================="

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
