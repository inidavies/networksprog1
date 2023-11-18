import socket
import sys
import time

def  client(hostname, port):
    # set hostname and port
    server_adress_port = (hostname, port)
    # Create a UDP socket
    client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    # Timeout set to 2 seconds
    client_socket.settimeout(3)  

    # Ping server 10 times
    for i in range(10):
        message = b'PING'
        client_socket.sendto(message, server_adress_port)
        print(f"PING {i+1}")

        # Listen for 
        try:
                response, server = client_socket.recvfrom(1024)
                print(f"Received '{response.decode()}' from {server}")
        except socket.timeout:
                print("Timeout: No response recieved") 
        
        time.sleep(1)

if __name__ == "__main__":
    #if len(sys.argv) != 3:
        #print("Usage: python client.py <hostname> <port>")
        #sys.exit(1)

    #hostname = sys.argv[1]
    #port = int(sys.argv[2])
    client('127.0.0.1', 20001)
