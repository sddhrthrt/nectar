import socket

def getCurrentIP(someip=""):
    if not someip:
        return -1
    master = someip
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((master, 80))
    ip = s.getsockname()[0]
    s.close()
    return ip
