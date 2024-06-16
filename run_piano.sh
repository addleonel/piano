#!/bin/bash

# Attempt to run the first option
echo "Trying first option..."
python3 /home/mendel/piano/ubuntu.py

# Check the exit status of the first option
if [ $? -ne 0 ]; then
    echo "First option failed. Trying second option..."
	python3 /home/leonel/dev/piano/ubuntu.py

fi
