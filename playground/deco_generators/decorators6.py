def decorator_function_with_arguments(arg1, arg2, arg3):
    def wrap(f):
        print("Inside wrap()")
        def wrapped_f(*args):
            print("Inside wrapped_f()")
            print("Decorator arguments", arg1, arg2, arg3)
            f(*args)
            print("After f(*args)")
        print("\n\nКінець конструктора\n\n")
        return wrapped_f
    return wrap


@decorator_function_with_arguments("Hello", "world", "42")
def sayHello(*args):
    print("sayHello arguments: ", *args)

print("Preparing to call sayHello()")
sayHello("say", "hello", "argument", "list")
print("after first sayHello() call")
sayHello("a", "different", "set of", "arguments")
print("after second sayHello() call")
