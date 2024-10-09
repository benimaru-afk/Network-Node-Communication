#Benjamin Mannal
# CSE 353 - Network Programming - Project 1
# 9/29/2024
# ---------------------
#Breif Description:
# This program is the code for Node B. It reads the port numbers of Node B and Node C from a file, 
# then receives data from Node A on the Node B port and sends it to Node C on the Node C port.
# ---------------------

import socket
import threading

# Function to handle receiving data from Node A and sending to Node C
def node_b():
    with open('confB.txt', 'r') as file:
        port_b = int(file.readline().strip())
        port_c = int(file.readline().strip())
        data = file.readlines()

    def receive_from_a():

        print("----")  # Beginning separator for readability in output

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                print(f"Node B listening on port {port_b} for data from Node A...")
                s.bind(('localhost', port_b))
                s.listen()
                conn, addr = s.accept()
                with conn:
                    while True:
                        data = conn.recv(1024)
                        if not data or data.decode() == 'stop':
                            break
                        print(f"Node B received: {data.decode().strip()}")
                    print("Node B finished receiving data from Node A.")
                    print("----")  # Separator for readability in output 

            except Exception as e:
                print(f"Node B encountered an error: {e}")

    def send_to_c():
        
        print("----")  # Beginning separator for readability in output

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.settimeout(5)
                print(f"Node B trying to connect to Node C on port {port_c}...")
                s.connect(('localhost', port_c))
                for line in data:
                    s.sendall(line.encode())
                s.sendall(b'stop')
                print("Node B finished sending data to Node C.")

            except socket.timeout:
                print(f"Node B: Connection to Node C on port {port_c} timed out.")
            except ConnectionRefusedError:
                print("Node B: Connection refused. Is Node C running?")
            except Exception as e:
                print(f"Node B encountered an error: {e}")

    threading.Thread(target=receive_from_a).start()
    threading.Thread(target=send_to_c).start()

if __name__ == "__main__":
    node_b()
