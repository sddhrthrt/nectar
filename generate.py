from Crypto.PublicKey import RSA
from ConfigParser import *

cp = ConfigParser()
cp.read('maf.conf')
masterip = cp.get('master', 'masterip')
hops = cp.get('itinerary', 'hops')
groute = []
hops = int(hops)
i=0
while hops > 0:
    attrname = "node" + str(i)
    groute.append(cp.get("itinerary", attrname))
    hops = hops - 1; i = i + 1

groute += [masterip]
print groute

def generateKeys(i):
    m = 'public'
    name = i.replace('.', '')+'_'+m+'.key'
    keys = RSA.generate(1024)

    f = open(name, 'w')

    p = keys.publickey()
    f.write(p.exportKey())
    f.close

    m = 'private'
    name = i.replace('.', '')+'_'+m+'.key'

    f = open(name, 'w')

    f.write(keys.exportKey())
    f.close

for i in groute:
    generateKeys(i)
