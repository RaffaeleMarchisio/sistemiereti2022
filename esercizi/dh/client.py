import random
import config
import time
import sys
import socket

def encode_big(num):
    return str(num).encode('utf8')
def decode_big(num):
    return int(num.decode('utf8'))
def mypow(a,b,n):
    acc=1
    while b>0:
        if b%2==1:
            acc=(acc*a)%n
        a=(a*a)%n
        b=b//2
    return acc
def dh(s):
    random.seed(2*int(time.time()))
    # Genero segreto
    a = random.randint(1, config.P-2)

    # Genero numero pubblico
    ga = mypow(config.G, a, config.P)
    s.sendall(encode_big(ga))

    gb = decode_big(s.recv(4096))

    gab = mypow(gb, a, config.P)

    print(gab)
def main(args):
    if len(args)<3:
        print(f"Usage:{args[0]} ip port")
        sys.exit(-1)
    address=(args[1],int(args[2]))
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.connect(address)
        gab=dh(s)


if __name__ == "__main__":
    main(sys.argv)
