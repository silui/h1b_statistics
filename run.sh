#!/bin/bash
#
# Use this shell script to compile (if necessary) your code and then execute it. Below is an example of what might be found in this file if your program was written in Python
#
#python ./src/h1b_counting.py ./input/h1b_input.csv ./output/top_10_occupations.txt ./output/top_10_states.txt

python $(pwd)/src/main.py states 10 $(pwd)/input/h1b_input.csv $(pwd)/output/top_10_states.txt
python $(pwd)/src/main.py occupations 10 $(pwd)/input/h1b_input.csv $(pwd)/output/top_10_occupations.txt