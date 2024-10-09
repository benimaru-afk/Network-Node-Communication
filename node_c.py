#Benjamin Mannal
# CSE 353 - Network Programming - Project 1
# 9/29/2024
# ---------------------
#Breif Description:
# This program is the code for Node C. It reads the port number of Node C from a file, then receives data from Node B on that port.
# ---------------------

import socket
import threading

# Function to handle receiving data from Node B
def node_c():
    with open('confC.txt', 'r') as file:
        port_c = int(file.readline().strip())

    print("----")  # Beginning separator for readability in output

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            print(f"Node C listening on port {port_c} for data from Node B...")
            s.bind(('localhost', port_c))
            s.listen()
            conn, addr = s.accept()
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data or data.decode() == 'stop':
                        break
                    print(f"Node C received: {data.decode().strip()}")
                print("Node C finished receiving data from Node B.")
                print("----")  # Separator for readability in output

        except Exception as e:
            print(f"Node C encountered an error: {e}")

if __name__ == "__main__":
    threading.Thread(target=node_c).start()
