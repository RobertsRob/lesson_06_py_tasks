fib = [0, 1]
def fibonacci(n):
    global fib
    if n <= len(fib):
        return fib[n-1]
    fib.append(fibonacci(n - 1) + fibonacci(n - 2))
    return fib[n-1]


print(fibonacci(40))




def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(40))
