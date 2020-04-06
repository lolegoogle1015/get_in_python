class decorator_without_arguments(object):

    def __init__(self, f):
        """
        If there are no decorator arguments, the function
        to be decorated is passed to the constructor.
        """
        print("Inside __init__()")
        self.f = f

    def __call__(self, *args):
        print("Inside __call__()")
        self.f(*args)
        print("After self.f(*args)")
        """
        The __call__ method is not called until the
        decorated function is called.
        """

@decorator_without_arguments
def sayHello(*args, **kwargs):
    print('sayHello arguments:', *args, **kwargs)

print("After decoration")

print("Preparing to call sayHello()")
sayHello('hi')
print("After first sayHello() call")
sayHello('man')
print("After second sayHello() call")
