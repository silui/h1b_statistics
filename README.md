# Table of Contents
1. [Problem](README.md#problem)
2. [Approach](README.md#Approach)
3. [Instructions](README.md#instructions)


# Problem

A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify the occupations and states with the most number of approved H1B visas. She has found statistics available from the US Department of Labor and its [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis). But while there are ready-made reports for [2018](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2018/H-1B_Selected_Statistics_FY2018_Q4.pdf) and [2017](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2017/H-1B_Selected_Statistics_FY2017.pdf), the site doesn’t have them for past years. 

As a data engineer, you are asked to create a mechanism to analyze past years data, specificially calculate two metrics: **Top 10 Occupations** and **Top 10 States** for **certified** visa applications.

Your code should be modular and reusable for future. If the newspaper gets data for the year 2019 (with the assumption that the necessary data to calculate the metrics are available) and puts it in the `input` directory, running the `run.sh` script should produce the results in the `output` folder without needing to change the code.

# Approach

First by opening .csv file into python as csv, it creates 2D list. Then start by getting iterating through all row with the targeted column and add to a frequency counter by 1 if that row is __CERTIFIED__. The built-in Counter() include most_common() property that return some number of most common elemnt. Then sort that list alphabetically in a tie. Finally, calculate the percentage of a particular state or occupation.

To future proof the program, I have __DICT__ at the beginning of main.py. In a case where USDOL decided to change file structure or column header name, user can add more to it.


# Instructions

To run scripts:
    h1b_statistics~$ ./run_tests.sh 

To run python scripts:
    h1b_statistics/src~$ python ./main.py HEADER #_of_top INPUTFILE OUTPUTFILE