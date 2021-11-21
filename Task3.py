from datetime import datetime


class Fibonacci:

    def __init__(self, element_number: int):
        self.el_num = element_number
        self.a = 0
        self.b = 1
        for i in range(3, self.el_num + 1):
            self.a, self.b = self. b, self.a + self.b

    def __save__(func):
        """
        Decorator method save method running result to file named same as Class
        :return:
        """

        def wrapper(*args, **kwargs):
            try:
                f = open(str(type(*args, **kwargs).__name__) + '.txt', 'a')
            except:
                f = open(str(type(*args, **kwargs).__name__) + '.txt', 'w')
            f.write(f'{func(*args, **kwargs)} - {datetime.now()}\n')
            f.close()
            return func(*args, **kwargs)

        return wrapper

    @__save__
    def __str__(self):
        if self.el_num == 1:
            return f'{self.el_num} member of Fibonacci sequence is {self.a}'
        else:
            return f'{self.el_num} member of Fibonacci sequence is {self.b}'


x = Fibonacci(5)
y = Fibonacci(7)
z = Fibonacci(9)

print(x)
print(y)
print(z)
