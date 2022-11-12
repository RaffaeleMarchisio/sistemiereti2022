import socket
import random
import time
import config

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

def dh(client):
    random.seed(int(time.time()))
    # Genero segreto
    b = random.randint(1, config.P-2)

    # Genero numero pubblico
    gb = mypow(config.G, b, config.P)
    client.sendall(encode_big(gb))

    ga = decode_big(client.recv(4096))

    gab = mypow(ga, b, config.P)
    print(gab)
def main():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0',5000))
        s.listen()
        client,client_address=s.accept()
        dh(client)

if __name__ == "__main__":
    main()

