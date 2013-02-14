#!/usr/bin/env python
#
# mafserv.py
#
#    - serve active agent
#
#

import SocketServer
from maflib import *

class maf_handler(SocketServer.BaseRequestHandler):
    def handle(self):
        import cPickle
        from migrate import *
        print "Receving incoming agent, verification is in process ..."
        print "From client:", self.client_address
        f = self.request.makefile()
        agent = cPickle.load(f)
        agent.localip = gethostname()
        agent.compLocal()
        agent.dispInfo()
        if (migrate(agent) == 0):
            print "\t Agent mission acomplished"
            return 0
        
def syncServer():
    serv = SocketServer.TCPServer(("",50001), maf_handler)
    try:
        print "Initialize MAF service, waiting for incoming agent ..."
        serv.serve_forever()
    except KeyboardInterrupt:
        goodbye()
   
# def asyncServer():


# main program
syncServer()
