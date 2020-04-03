###########################   Decorators   ###############################
"""def decorator(func):
    return func

@decorator
def decorated():
    print("hello")

decorated = decorator(decorated)"""

"""
def decorator(func):
    def new_func():
        pass
    return new_func

@decorator
def decorated():
    print("Hello")

decorated()

print(decorated.__name__)
Output: 'new_func'
"""
#Функція, яка приймає та модикіфує її та повертає її ж
