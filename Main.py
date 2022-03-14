import sys
import copy
import TestSuite
import QuickSort
import QuickSort_not_Optomized as Quick_n
import QuickSort_It
import BubbleSort
import MergeSort
import TimSort

sys.setrecursionlimit(5000)
file_name = 'Test_Output.txt'

n = 1000000 #run BubbleSort at size 100,000 to get conclusive data as it scales
test_data = TestSuite.generate_data(n)

#with open(file_name,'a') as f:
#    print('----------------Testing BubbleSort----------------\n', file=f)
#TestSuite.time_sort(n, BubbleSort.sort,test_data,file_name)

run_data = copy.deepcopy(test_data)
with open(file_name,'a') as f:
    print('----------------Testing MergeSort----------------\n', file=f)
TestSuite.time_sort(n, MergeSort.sort,run_data,file_name)

run_data = copy.deepcopy(test_data)
with open(file_name,'a') as f:
    print('----------------Testing TimSort----------------\n', file=f)
TestSuite.time_sort(n, TimSort.timSort,run_data,file_name)

run_data = copy.deepcopy(test_data)
with open(file_name,'a') as f:
    print('----------------Testing QuickSort----------------\n', file=f)
TestSuite.time_sort(n, QuickSort_It.sort,run_data,file_name)

with open(file_name,'a') as f:
    print('------------------------------------------------\n----------------Test Complete------------------\n------------------------------------------------', file=f)
