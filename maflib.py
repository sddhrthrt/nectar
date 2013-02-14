# maflib.py -
#
#    includes a set of common utilities for MAF
# 
# Author: Feiyi Wang
#         fwang2@mcnc.org
#
# Copyright (C) 2001
#
# $Id: maflib.py,v 1.1.1.1 2001/04/17 17:53:45 fwang2 Exp $

import asyncore
import string, os, stat,sys
from socket import *

def goodbye():
    print "\n\n"
    print '\t==========================================='
    print '\t=    Interrupt Key Detected, Goodbye!     ='
    print "\t=          **********************         ="
    print "\t=              M A F  D E M O             ="
    print '\t==========================================='

def printfile(f):
    print '\t==========================================='
    while 1:
        line = f.readline()
        print '\t', line
        if not line: break
    print '\t==========================================='
    

def sndTCPFile(file, ipaddr, port):
    try:
        mf = open(file, "r")
    except IOError, e:
        print "Unable to open:", file, e
        sys.exit(1)
        
    # now read the file content into a string
    mstr = mf.read()
    
    try:
        s = socket(AF_INET, SOCK_STREAM)
    except:
        print "Oh well, something wrong with creating socket"
        sys.exit(1)

    # we need a non-blocking I/O here
    connected = s.connect_ex((ipaddr, port))
    if (connected == 0):
        outbytes = s.send(mstr)
        print "\n\n\t\t=> Good! ", outbytes, \
              "bytes has been sent to ", ipaddr
        return 0
    else:
        print "\n\n\t\t=> Oh, no, couldn't connected with ", ipaddr
        return -1
    

def sndTCPMsg(mstr, ipaddr, port):
    
    try:
        s = socket(AF_INET, SOCK_STREAM)
    except:
        print "Oh well, something wrong with creating socket"
        sys.exit(1)

    # we need a non-blocking I/O here
    connected = s.connect_ex((ipaddr, port))
    if (connected == 0):
        outbytes = s.send(mstr)
        print "\n\n\t\t=> Good! ", outbytes, \
              "bytes has been sent to ", ipaddr
        return 0
    else:
        print "\n\n\t\t=> Oh, no, couldn't connected with ", ipaddr
        return -1
