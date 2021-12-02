# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.
import cProfile


def algo_without_eratosphen(number):
    final_list = []
    for some_number in range(number):
        if some_number > 1:
            for true_number in range(some_number):
                if true_number > 1 and some_number % true_number == 0:
                    break
            else:
                final_list.append(some_number)

    return final_list


def find_number_in_algo_without_eratosphen(i, erat_number):
    abce = algo_without_eratosphen(erat_number)
    for ind_z, z in enumerate(abce):
        if ind_z+1 >= i:
            return z


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


def find_number_in_algo_eratosphen(i, erat_number):
    abce = eratosphen(erat_number)
    for ind_z, z in enumerate(abce):
        if ind_z + 1 >= i:
            return z


cProfile.run('find_number_in_algo_without_eratosphen(50, 7000)')
cProfile.run('find_number_in_algo_eratosphen(50, 7000)')


"""
Как показали измерения, алгоритм основанный на решере Эратосфена, работает быстрее на больших объемах данных.
Ниже результат измерения работы без использования «Решета Эратосфена»:
cProfile.run('find_number_in_algo_without_eratosphen(50, 7000)')

         905 function calls in 0.143 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.143    0.143 4_2.py:22(find_number_in_algo_without_eratosphen)
        1    0.143    0.143    0.143    0.143 4_2.py:9(algo_without_eratosphen)
        1    0.000    0.000    0.143    0.143 <string>:1(<module>)
        1    0.000    0.000    0.143    0.143 {built-in method builtins.exec}
      900    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Ниже результат измерения работы с использованием «Решета Эратосфена»:
cProfile.run('find_number_in_algo_eratosphen(50, 7000)')

         7 function calls in 0.002 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.001    0.001 4_2.py:29(eratosphen)
        1    0.000    0.000    0.000    0.000 4_2.py:30(<listcomp>)
        1    0.000    0.000    0.000    0.000 4_2.py:42(<listcomp>)
        1    0.000    0.000    0.001    0.001 4_2.py:46(find_number_in_algo_eratosphen)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



Process finished with exit code 0


"""