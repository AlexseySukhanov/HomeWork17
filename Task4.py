from datetime import datetime
from time import sleep


def time_tester(file_name: str, repetitions: int):
    """
    Decorator for function time testing , measure time if function running and writes it to file
    :param file_name: file name for results if time measuring
    :param repetitions: number if function running's
    :return: time of function running
    """

    f = open(file_name, 'w')

    def func_run(func):
        def wrapper(*args, **kwargs):
            tmp = datetime.now()
            total_time = tmp
            total_time = total_time - tmp

            for i in range(repetitions):
                time_start = datetime.now()
                func(*args, **kwargs)
                time_stop = datetime.now()
                total_time += time_stop - time_start
                f.write(f'Function {func.__name__} run № {i+1} time of function running {time_stop-time_start}\n')
            f.write(f'Total running time is {total_time}')
            f.close()

            return func(*args, *kwargs)
        return wrapper
    return func_run


@time_tester('time_test.txt', 10)
def fibo():
    """
    Wrapped memorized function calculates Fibonacci number
    :return: Fibonacci number of n elements
    """
    result = {}
    a = 0
    b = 1

    def wrap(n):
        nonlocal result
        nonlocal a
        nonlocal b
        if result.get(n):
            return result.get(n)
        else:
            for i in range(3, n+1):
                a, b = b, a + b
            return b
    sleep(1)  #delay 1 second
    return wrap


numbers = fibo()
print(numbers(40))
