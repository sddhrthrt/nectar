class CompLocal:
    def __init__(self):
        self.totalfree=[]
        return

    def compute(self):
        import UnixShell, string, StringIO
        # do some real work here
        result = UnixShell.getCommandOutput("df")
        fd = StringIO.StringIO(result)
        for line in fd.readlines():
            if line[0] != 'F': # skip the first line
                words = string.split(line) # extract fourth column
                if len(words) == 6:
                    self.totalfree = self.totalfree + [int(words[3])]
                elif len(words) == 5:
                    self.totalfree = self.totalfree + [int(words[2])]
                else:
                    print "\t Unexpected output from shell"
        return self.totalfree

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        print "comparing"
        return self.__dict__ == other.__dict__
