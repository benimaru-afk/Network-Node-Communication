# Network-Node-Communication
Project 1 for CSE353

The aim of this project is to practice inter-process communication via TCP/IP sockets. The project is an
initial stage to prepare for the main semester two projects. It will utilize the TCP/IP sockets to emulate
the physical layer links which will be used in the final projects.

README - Benjamin Mannal - CSE 353 - Project 1:

How to Run the Code:

1. Open Bash/WSL Terminal.

2. Navigate to the directory where all project files are stored.
   - Example command: cd /path/to/your/project-directory

3. Confirm all files are present:
   The directory should contain the following files:
   - node_a.py, node_b.py, node_c.py, confA.txt, confB.txt, confC.txt, Makefile

4. Run the program using the Makefile.
   - Enter the following command in your terminal:
     'make all'
   This should initiate the nodes and run the program.

5. Expected Output:
   You should see an output similar to this:

   brmannal@BensLaptop:/mnt/c/Users/benma/OneDrive/Desktop/cse353/ProjectBRM$ make all
   python3   node_c.py & 
   python3   node_b.py &
   python3   node_a.py
   ----
   Node C listening on port 5001 for data from Node B...
   Node C encountered an error: [Errno 98] Address already in use
   ----
   Node A trying to connect to Node B on port 5000...
   ----
   Node B listening on port 5000 for data from Node A...
   Node A finished sending data.
   ----
   ----
   Node B received: This is a sample data from Node A.
   The next lecture after the due date of project 1 is Oct-1st.stop
   Node B finished receiving data from Node A.
   ----
   Node B encountered an error: [Errno 98] Address already in use
   Node B trying to connect to Node C on port 5001...
   Node B finished sending data to Node C.
   Node C received: This is a sample data from Node B.
   This the first project of CSE 353!
   I love learning about networking!!stop
   Node C finished receiving data from Node B.
   ----

6. Enjoy! :)
