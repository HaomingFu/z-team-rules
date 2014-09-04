class entryExit(object):
    def __init__(self, f):
        self.f = f
    def __call__(self, *args):
        print("entering function", self.f.__name__)
        self.f(*args)
        print("exited", self.f.__name__)

@entryExit
def fun1(a, b):
    print("in function 1")
    print(a+b)


@entryExit
def fun2():
    print("in function 2")

fun1(3, 4)
fun2()
