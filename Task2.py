func_list = []


def register(func):
    """
    Decorator for function, register name of running function in global func_list
    :param func: Function
    :return: Function return
    """

    global func_list

    def wrapper(*args, **kwargs):
        func_list.append(func.__name__)
        return func(*args, **kwargs)
    return wrapper


@register
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
print(func_list)
