# Makefile for CSE 353 Project 1
#Benjamin Mannal
# 9/29/2024
# ---------------------
#Breif Description:
# This Makefile is used to run the three nodes in the correct order. It will establish nodes C and B in the background, 
# and then run node A. The Makefile also includes two delay targets to give the nodes time to start and process. 
# The clean target is used to remove any temporary files that may have been created.
# ---------------------

PYTHON = python3  # Use python3 for WSL

NODE_A = node_a.py
NODE_B = node_b.py
NODE_C = node_c.py

# Default target to run all nodes in the correct order
all: node_c delay node_b delay2 node_a

# Target to run Node A
node_a:
	$(PYTHON) $(NODE_A)

# Target to run Node B
# Use '&' to run it in the background
node_b:
	$(PYTHON) $(NODE_B) &

# Target to run Node C in the background
# Use '&' to run it in the background
node_c:
	$(PYTHON) $(NODE_C) & 

delay:
	sleep 2

delay2:
	sleep 2

# Clean up any temporary files (if any were created)
clean:
	rm -f *.pyc __pycache__/*
