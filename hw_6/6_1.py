from memory_profiler import profile


def eratosphen(n):
    start_list = [i for i in range(n)]
    start_list[1] = 0

    m = 2
    while m < n:
        if start_list[m] != 0:
            j = m * 2
            while j < n:
                start_list[j] = 0
                j = j + m
        m += 1

    final_list = [i for i in start_list if i != 0]
    return final_list


@profile()
def find_number_in_algo_eratosphen(i, erat_number):
    abce = eratosphen(erat_number)
    return abce[i-1]


print(find_number_in_algo_eratosphen(50, 770000))


"""
Python 3.8
OS - 64 bit

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    21     16.2 MiB     16.2 MiB           1   @profile()
    22                                         def find_number_in_algo_eratosphen(i, erat_number):
    23     46.3 MiB     30.1 MiB           1       abce = eratosphen(erat_number)
    24     46.3 MiB      0.0 MiB           1       return abce[i-1]

"""