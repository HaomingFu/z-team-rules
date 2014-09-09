"""
Bottom up DP to calculate fibonacci number
"""
def fibonacci(n):
    fib = {}
    for k in range(1, n+1):
        if k <= 2:
            f = 1
        else:
            f = fib[k-1] + fib[k-2]
        fib[k] = f
    return fib[n]

def test():
    print(fibonacci(22))

test()
