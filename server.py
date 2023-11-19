import socket
from random import randint

def  server(hostname, port):
    # set hostname and port
    server_adress_port = (hostname, port)

    # Create a UDP socket
    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Bind to address and ip
    server_socket.bind(server_adress_port)

    print('Inioluwa Davies iod0007')
    print(f"Server listening on {hostname}:{port}")
    print("[server] : ready to accept data...")

    while True:
        # Listen for incoming datagrams
        #bufferSize, 1024
        response, client = server_socket.recvfrom(1024)
        print("[client] : PING")
        
        # Dropping packets with a 30% chance so, 70% response rate
        r  = randint(1,10)
        if  r < 3:
            print('packet dropped')
        else:
            response =  b'PONG'
            server_socket.sendto(response, client)
            #print(f"Sent 'PONG' to {client}")
 
if __name__ == "__main__":
    server('127.0.0.1', 20001)