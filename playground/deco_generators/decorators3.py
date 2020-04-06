def entry_exit(f):
    def inner(*args, **kwargs):
        print("Entering", f.__name__)
        f()
        print("Exited", f.__name__)
    return inner

@entry_exit
def func1():
    print("inside func1()")

@entry_exit
def func2():
    print("inside func2()")


func1()
func2()
print(func1.__name__)
