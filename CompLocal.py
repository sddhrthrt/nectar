class CompLocal:
    def __init__(self):
        self.totalfree=[]
        return

    def compute(self):
        from time import sleep
        import UnixShell, string, StringIO
        #sleep
        print "sleeping..."
        sleep(2)
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
                    print "Unexpected output from shell"
        self.totalfree = [sum(self.totalfree), ]
        return self.totalfree

    def __eq__(self, other):
        print "comparing"
        return self.__dict__ == other.__dict__
