from __future__ import division
import csv,sys
from collections import Counter

assert len(sys.argv)==5, 'usage: progname target_header TOPCOUNT INPUTFILEPATH OUTPUTFILEPATH\n available target_header: states, occupations'

# DICT translate arg to column header and output header
# If column header is not included in dict, please add the exact header to the corresponding arg
#DICT = {argv:[LIST OF INPUT HEADER NAME],OUTPUT_HEADER_NAME}
DICT = {
    'states': (['WORKSITE_STATE','LCA_CASE_WORKLOC1_STATE'],'TOP_STATES'),
    'occupations': (['LCA_CASE_SOC_NAME','SOC_NAME'],'TOP_OCCUPATIONS'),
    'status': (['CASE_STATUS','STATUS'],''),
    }


# find header index given header argv
def column_index_finder(row,targetString):
    assert targetString in DICT, "argument not found"
    for header in DICT[targetString][0]:
        if(header in row):
            return row.index(header)
    raise ValueError('column header is not found given arg')
    
# sort and build output string
def output_builder(arr):
    # sort list of tuple alphabetically in a tie, takin advantage of python sort is stable
    arr.sort(key=lambda x: x[0])
    arr.sort(key=lambda x: x[1],reverse=True)
    returnThis = DICT[sys.argv[1]][1] + ';NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n'
    sum_case = sum(map(lambda x : x[1],arr))
    for tup in arr:
        returnThis+=tup[0]+';'+str(tup[1])+';'+str(round(tup[1]*100/sum_case,1))+'%\n'
    return returnThis

input_arr = []
with open(sys.argv[3]) as csvfile:
    spamreader = csv.reader(csvfile,delimiter=';')
    for row in spamreader:
        input_arr.append(row)
target_index = column_index_finder(input_arr[0],sys.argv[1])
status_index = column_index_finder(input_arr[0],'status')
frequency_counter = Counter()
for i in range(1,len(input_arr)):
    if(input_arr[i][status_index]=='CERTIFIED'):
        frequency_counter[input_arr[i][target_index]] += 1
outputfile = open(sys.argv[4],"w")
outputfile.write(output_builder(frequency_counter.most_common(int(sys.argv[2]))))
outputfile.close()