#!/usr/bin/env python
#
# maf.py - Mobile Agent Framework
#          
#          This program is used to demostrate python language "active"
#          object and some network capability. According to a
#          present route, MAF agent starts from local machine, peform
#          a fixed set of task (example: number of current users) on
#          each node, and return back with the result.
#
# Author -
#         fwang2@mcnc.org
#         Copyright (C) 2001
#
# Basic algorithm:
#
#
#
import os, string, sys, getopt
from migrate import *
from DiskAgent import *
import rsa
import cPickle

def mafinit(confname):
    from ConfigParser import *
    # set up environment
    # global variable has to be declared this way
    global groute,masterip
    groute = []
    if os.path.exists(confname):
        cp = ConfigParser()
        cp.read(confname)
        # Comments:
        # temp variable i is for composing node0,node1 ...
        # master ip is for nexthop control
        # hops, of course is to define how many nodes you have
        # to travel, just make life a bit easier, can be skipped
        i = 0
        masterip = cp.get("master","masterip")
        hops = cp.getint("itinerary", "hops")
        while hops > 0:
            attrname = "node" + str(i)
            groute.append(cp.get("itinerary", attrname))
            hops = hops - 1; i = i + 1
    else:
        print "Can not find required configuration file\n"
        sys.exit(1)

#### main program starts
mafinit("maf.conf")

#### create new agent
agentx = DiskAgent(masterip,groute)
#### Sign the agent

binstr = cPickle.dumps(agentx.compLocal, 1)
(priv, pub) = rsa.newkeys(512)
agentx.serverSignature = rsa.sign(binstr, priv, 'MD5')
agentx.serverPubKey = pub

#### display some information related to this agent
agentx.dispInfo()

#### migrate this agent
migrate(agentx)

