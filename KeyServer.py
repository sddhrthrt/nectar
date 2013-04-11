from Crypto.PublicKey import RSA

def getPublicKey(ip):
    f = open(ip.strip().replace('.', '')+'_public.key')
    return RSA.importKey(f.read())

def getPrivateKey(ip):
    f = open(ip.strip().replace('.', '')+'_private.key')
    return RSA.importKey(f.read())
