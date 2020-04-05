"""Decorators with files
def logger(filename):
    def decorator(func):
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'w') as f:
                f.write(str(result))
            return result
        return wrapped
    return decorator

@logger('new_log.txt')
def summator(num_list):
    return sum(num_list)

#summator = logger('log.txt')(summator)

summator([1, 2, 3, 4, 5, 6])

with open('new_log.txt', 'r') as f:
    print(f.read())
"""

def first_decorator(func):
    def wrapped():
        print('Inside first_decorator product')
        return func()
    return wrapped

def second_decorator(func):
    def wrapped():
        print('Inside second_decorator product')
        return func()
    return wrapped

@first_decorator
@second_decorator
def decorated():
    print("Finally called...")

decorated()
