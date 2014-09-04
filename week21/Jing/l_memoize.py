import functools
def memoize(obj):
    cache = obj.cache = {}
    print(obj)
    print(cache)

    @functools.wraps(obj)
    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            print("not in cache!!")
            cache[key] = obj(*args, **kwargs)
        return cache[key]
    return memoizer

@memoize
def f(a, b):
    return a**b

def test():
    print(f(1,2))
    print(f(4,5))
    print(f(1,2))

