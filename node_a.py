#Benjamin Mannal
# CSE 353 - Network Programming - Project 1
# 9/29/2024
# ---------------------
#Breif Description:
# This program is the code for Node A. It reads the port number of Node B from a file, then sends data to Node B on that port.
# ---------------------

import socket
import threading

# Function to handle sending data from Node A to Node B
def node_a_send():
    with open('confA.txt', 'r') as file:
        port_b = int(file.readline().strip())
        data = file.readlines()

    print("----")  # Beginning separator for readability in output

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.settimeout(5)
            print(f"Node A trying to connect to Node B on port {port_b}...")
            s.connect(('localhost', port_b))
            
            for line in data:
                s.sendall(line.encode())
            s.sendall(b'stop')
            print("Node A finished sending data.")
            print("----")  # Separator for readability in output

        except socket.timeout:
            print(f"Node A: Connection to Node B on port {port_b} timed out.")
        except ConnectionRefusedError:
            print("Node A: Connection refused. Is Node B running?")
        except Exception as e:
            print(f"Node A encountered an error: {e}")

if __name__ == "__main__":
    threading.Thread(target=node_a_send).start()
