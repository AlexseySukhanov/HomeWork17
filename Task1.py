def counter(func):
    """
    Decorator for function calculates how many times function runs
    :param func: Function
    :return: how many times function runs
    """
    i = 0

    def wrapper(*args, **kwargs):
        nonlocal i
        i += 1
        return f'Function run {i} times, result: {func(*args, **kwargs)}'
    return wrapper


@counter
def summa(a, b):
    """
    Calculates sum of two numbers
    :param a: number (integer or float)
    :param b: number (integer or float)
    :return: number (integer or float)
    """
    return a + b


print(summa(1, 2))
print(summa(3, 4))
