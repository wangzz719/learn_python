class DecoratorWithArguments(object):

    def __init__(self, arg1, arg2, arg3):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        print "Inside __init__()"
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """
        print "Inside __call__()"

        def wrapped_f(*args):
            print "Inside wrapped_f()"
            print "Decorator arguments:", self.arg1, self.arg2, self.arg3
            f(*args)
            print "After f(*args)"
        return wrapped_f


@DecoratorWithArguments("hello", "world", 42)
def say_hello(a1, a2, a3, a4):
    print 'sayHello arguments:', a1, a2, a3, a4

print "After decoration"

print "Preparing to call say_hello()"
say_hello("say", "hello", "argument", "list")
print "after first say_hello() call"
say_hello("a", "different", "set of", "arguments")
print "after second say_hello() call"


def decorator_function_with_arguments(arg1, arg2, arg3):
    def wrap(f):
        print "Inside wrap()"

        def wraped_f(*args):
            print "Inside wrapped_f()"
            print "Decorator argumens:", arg1, arg2, arg3
            f(*args)
            print "After f(*args)"
        return wraped_f
    return wrap


@decorator_function_with_arguments("hello", "world", 45)
def say_hello_2(a1, a2, a3, a4):
    print "say_hello_2 arguments:", a1, a2, a3, a4

print "After decoration"

print "Preparing to call say_hello_2()"
say_hello_2("say", "hello", "argument", "list")
print "after first say_hello_2() call"
say_hello_2("a", "different", "set of", "arguments")
print "after second say_hello_2() call"
