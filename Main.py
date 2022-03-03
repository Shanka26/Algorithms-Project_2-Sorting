import TestSuite
import QuickSort
import BubbleSort
import MergeSort
import TimSort

n = 10000
file_name = 'Test_Output.txt'
test_data = TestSuite.generate_data(n)
with open(file_name,'a') as f:
    print('----------------Testing BubbleSort----------------\n', file=f)
TestSuite.time_sort(n, BubbleSort.sort,test_data,file_name)

with open(file_name,'a') as f:
    print('----------------Testing MergeSort----------------\n', file=f)
TestSuite.time_sort(n, MergeSort.sort,test_data,file_name)

with open(file_name,'a') as f:
    print('----------------Testing TimSort----------------\n', file=f)
TestSuite.time_sort(n, TimSort.timSort,test_data,file_name)

with open(file_name,'a') as f:
    print('----------------Testing QuickSort----------------\n', file=f)
TestSuite.time_sort(n, QuickSort.sort,test_data,file_name)
