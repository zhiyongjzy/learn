

def sub(x, y):
    return x-y

def func(n):
    return abs(n)

def func_d(arg1, arg2):
    def outter(fn):
        def inner(x, y):
            print("1111 {}, {}".format(arg1, arg2))
            return abs(fn(x, y))
        return inner
    return outter

@func_d("arg1", "arg2")
def sub_d(x, y):
    print("---")
    return x-y

if __name__ == "__main__":
    print(abs(sub(3,5)))
    print("分界符")
    print(sub_d(3,5))

