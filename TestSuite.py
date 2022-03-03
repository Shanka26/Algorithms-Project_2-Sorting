import random
import math
import timeit

def generate_data(n):
    #generate test data--ordered, semi-ordered, and random each for every order of magnitude from 1 to log(n)
    max_magnitude = int(math.log10(n))
    test_data = []
    for i in range(1, max_magnitude+1):
        #ordered data
        test_data.append([10**i, 'ordered'])
        ordered_data = []
        for j in range(0, 10**i):
            ordered_data.append(j)
        test_data.append(ordered_data)

        #semi-ordered data
        test_data.append([10**i,'semi-ordered'])
        stage_list = []
        segment_size = int(2*10**(math.ceil(i/3)-1))
        num_segments = int((10**i)/segment_size)
        for j in range( 0, num_segments):
            stage_list.append(j)
        random.shuffle(stage_list)
        semiordered_data = []
        for j in range(0, num_segments):
            for k in range(1, segment_size + 1):
                semiordered_data.append((stage_list[j] * segment_size) + k)
        test_data.append(semiordered_data)


        #random data
        test_data.append([10**i, 'random'])
        random_data = []
        for j in range(0, 10**i):
            random_data.append(j)
        random.shuffle(random_data)
        test_data.append(random_data)

    return test_data

def time_sort(n, sort, data, file_name):
    magnitudes = int(math.log10(n))
    with open(file_name, 'a') as f:
        for i in range(0, magnitudes):
            for j in range(0,3):
                print('Timing sort on ' + str(data[(6*i)+(2*j)][1]) + ' data of size ' + str(data[(6*i)+(2*j)][0]) + ':', file=f)
                start_time = timeit.default_timer()
                sort(data[(6*i)+(2*j+1)])
                run_time = timeit.default_timer() - start_time
                print('Sort executed in ' + str(run_time) + ' seconds.\n', file=f)
                







