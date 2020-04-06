# Now a few lines needed to make simple_decorator itself
# be a well-behaved decorator.
def simple_decorator(decorator):#my_simple_logging_decorator
    print(1)
    def new_decorator(f):#double func
        print(2)
        g = decorator(f)#my_simple_logging_decorator(x)
        print(3)
        print(g.__name__)
        g.__name__ = f.__name__
        print(4)
        print(g.__name__)
        g.__doc__ = f.__doc__
        print(5)
        g.__dict__.update(f.__dict__)
        print(6)
        return g
    print(new_decorator.__name__)
    new_decorator.__name__ = decorator.__name__
    print(new_decorator.__name__)
    print(7)
    new_decorator.__doc__ = decorator.__doc__
    print(8)
    new_decorator.__dict__.update(decorator.__dict__)
    print(9)

    return new_decorator


#
#Sample Use:
#Декоратор для декоратора
@simple_decorator
def my_simple_logging_decorator(func):
    print(10)
    def you_will_never_see_this_name(*args, **kwargs):
        print(11)
        print('calling {}'.format(func.__name__))
        print(12)
        return func(*args, **kwargs)
    print(13)
    return you_will_never_see_this_name

@my_simple_logging_decorator
def double(x):
    'Doubles a number.'
    print(14)
    return x * 2

assert double.__name__ == 'double'
assert double.__doc__ == 'Doubles a number.'

#double = simple_decorator(my_simple_logging_decorator(double))

print(double(155))
