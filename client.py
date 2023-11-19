import socket
import sys
import time

def  client(hostname, port):
    # set hostname and port
    server_adress_port = (hostname, port)
    # Create a UDP socket
    client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    # Timeout set to 3 seconds
    client_socket.settimeout(3)

    print('Inioluwa Davies iod0007')  

    # Ping server 10 times
    for i in range(10):
        message = b'PING'
        client_socket.sendto(message, server_adress_port)

        # Listen for 
        try:
                response, server = client_socket.recvfrom(1024)
                print(f"{i+1} : Sent PING... received b'PONG'")
        except socket.timeout:
                print(f"{i+1} : Sent PING... Timed out") 
        
        time.sleep(1)

if __name__ == "__main__":
    client('127.0.0.1', 20001)
