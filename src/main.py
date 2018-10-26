import csv,sys
from collections import Counter

# dict translate arg to column header
# If column header is not included dict, please add the exact header to the corresponding arg
def column_index_finder(row,targetString):
    dict = {
        'state': ['EMPLOYER_STATE','LCA_CASE_EMPLOYER_STATE'],
        'occupations': ['LCA_CASE_JOB_TITLE','JOB_TITLE']
    }
    assert targetString in dict, "argument not found"
    for header in dict[targetString]:
        if(header in row):
            return row.index(header)
    raise ValueError('column header is not found given arg')
    


input_arr = []
# with open('../input/test.csv') as csvfile:
with open('../input/H1B_FY_2014.csv') as csvfile:
    spamreader = csv.reader(csvfile,delimiter=';')
    for row in spamreader:
        input_arr.append(row)
target_index = column_index_finder(input_arr[0],sys.argv[1])
frequency_counter = Counter()
for i in range(1,len(input_arr)):
    frequency_counter[input_arr[i][target_index]] += 1
print(frequency_counter.most_common(10));
