
"""class B(Exception):
    pass


class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")

    except C:
        print("C")

    except B:
        print("B")

class Error(Exception):
    pass

class InpuError(Error):
    Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error


    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    Raised when an operator attempts a state transition that is not allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed


    def __init__(self, previous, next, message):
        self.previous = previous
        self. next = next
        self.message = message"""
"""
try:
    raise KeyboardInterrupt
except KeyboardInterrupt:
    pass
finally:
    print('Goodbye, world!')"""

"""

****Помилки, які виникають під час виконання блоку try можуть бути спійманими
    блоком except. Однак, якщо помилка не була спіймана, через відсутність блоку except, або через неспівпадіння типу помилки
    блок finally завершиться як остання дія блоку try, а після цього
    помилка буде зарейзена.

    def divide(x, y):
        try:
            result = x / y
        except ZeroDivisionError:
            print("division by zero!")
        else:
            print("result is ", result)
        finally:
            print("executing finally clause")

    divide(2,1)
    divide(2, 0)
    divide("2", "1")

****If the try statement reaches a break, continue or return statement, the finally clause will execute just
    prior to the break, continue or return statement’s execution.

****Якщо блок finally return-ить значення, то це буде його власне значення, а не return блоку try.

    def bool_return():
        try:
            return True
        finally:
            return False

    print(bool_return())

"""
