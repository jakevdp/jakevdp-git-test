def print_hello_world():
    print('hello world!')


def fib(n):
    fibs = []
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        fibs.append(a)
    return fibs

print_hello_world()
print(list(fib(10)))
