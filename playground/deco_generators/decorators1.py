"""def myDecorator(func):
    def inner(*args, **kwargs):
        print (func(*args, **kwargs))
        print("The positional arguments: {}\n The keyword arguments: {}".format(*args, **kwargs))
    return inner

@myDecorator
def sum_function(a, b):
    return a + b

print(sum_function.__name__)"""

class my_decorator(object):

    def __init__(self, f):
        print("Декорування...")
        print("Inside my decorator.__init__()")
         # Prove that function definition has completed

    def __call__(self):
        print("Викликаємо функцію, чий метод кол ми перевизначили")
        print("Inside my_decorator.__call__()")

@my_decorator
def aFunction():
    print('Inside aFunction')

print("Finished decorating aFunction()")

aFunction()

#def foo(): pass
#foo = staticmethod(foo)
#@staticmethod
#def foo(): pass













#Єдине обмеження в декораторах це те, що повертаємий об'єкт повинен бути callable
#Так як я використою класт, то будь-який клас, який ми використовуємо як декоратор повинен містити метод __call__
