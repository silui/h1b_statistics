#!/bin/bash

python ./src/main.py states 10 ./input/h1b_input.csv ./output/top_10_states.txt
python ./src/main.py occupations 10 ./input/h1b_input.csv ./output/top_10_occupations.txt