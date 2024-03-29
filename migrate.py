#
# migrate.py -
#
#    migrate "agent" to "whereip" at "port"
#
from AgentCareer import AgentCareer

def nexthop(agent):
    #
    # Function description:
    #
    #   return next ip address
    #
    # Basic algorithm:
    #
    #   IF   localip is not in the list
    #        THEN report error
    #   ELIF localip is the last item
    #        THEN stop migration, report final
    #   ELSE return next ip address
    #
    # This algorithm requires to have a complete loop
    # defined

    # Addition note:
    #
    #   It is a bit tricky to define a no-loop return of ip,
    #   and the following logic is what I intended, but not
    #   necessarily so
    #
    import sys

    lastip = agent.route[len(agent.route) - 1]

    #if agent.localip not in agent.route:
        #print "\t Something is wrong, local ip is NOT in route, abort!"
        #return -1
    #elif (agent.localip == agent.route[0]) and (len(agent.route)==1):
    #    print "\t Local ip is the only item, stop migration"
    #    return 0
    #elif (agent.localip == lastip) and (agent.hops!=0):
    #    print "\t Local ip is the last item, stop migration"
    #    return 0
    if agent.hops > len(agent.route):
        print "\t agent is back!"
        return 1
    elif (agent.localip == lastip) and (agent.hops!=0):
        print "\t Local ip is the last item, stop migration"
        return 0
    elif agent.hops==0:
        print "\t A very first hop, just first ip"
        return agent.route[0]
    else:
        nextip = agent.route[agent.route.index(agent.localip) + 1]
        print "\tNormal case, return next ip", nextip
        return nextip

def migrate(agent):
    # port number can be more flexiably defined
    # for now, we assume that this is a fixed and
    # well-known port
    from socket import *
    from maflib import *
    import cPickle, sys
    nextip = nexthop(agent)
    if nextip == -1:
        print "I can't find a valid next hop, abort!"
        return -1
    elif nextip==1:
        #it reached back the server .
        print "==== =========================== ==="
        print "I'm done!"
        print "==== =========================== ==="
        return 0
    elif nextip == 0:
        #last node, now send it back to the master
        print "==== =========================== ==="
        print "==== Agent Work Done, returning. ==="
        print "==== =========================== ==="
        agent.dispInfo()
        nextip = agent.masterip
    print "\t migrate to :", nextip
    bin = 1; agent.hops = agent.hops + 1
    career = AgentCareer(agent, nextip)
    career.readyToTransport()
    binstr = cPickle.dumps(career, bin)
    sndTCPMsg(binstr,nextip,50001)
