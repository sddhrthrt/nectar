#
# define a specialized agent which knows how to collect
# hard disk usage statistics
#

class DiskAgent:

    def __init__(self,masterip,route):
        from socket import *
        import PlusAgent

        self.masterip = masterip
        self.totalfree = 0
        self.route = route
        self.hops = 0
        self.localip = "192.168.56.1"
        self.plusval = PlusAgent.selfplus(0)

    def dispInfo(self):
        import PlusAgent
        # print out the result
        print "\t ================================="
        print "\t         Agent Information        "
        print "\t ================================="
        print "\t free disk space:", self.totalfree
        print "\t local ip is :", self.localip
        print "\t master ip is:", self.masterip
        print "\t current hops is:",self.hops
        print "\t planned route is:", self.route
        print "\t self plus result is", PlusAgent.dispvar()
        print "\t ================================="

    def compLocal(self):
        import UnixShell, string, StringIO, PlusAgent
        # Plus work
        self.plusval = PlusAgent.selfplus(self.plusval)
        # do some real work here
        result = UnixShell.getCommandOutput("df")
        fd = StringIO.StringIO(result)
        for line in fd.readlines():
            if line[0] != 'F': # skip the first line
                words = string.split(line) # extract fourth column
                if len(words) == 6:
                    self.totalfree = self.totalfree + int(words[3])
                elif len(words) == 5:
                    self.totalfree = self.totalfree + int(words[2])
                else:
                    print "\t Unexpected output from shell"
        return self.totalfree
