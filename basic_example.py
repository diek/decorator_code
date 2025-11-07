def simple_decorator(func):
    def wrapper():
        print(">>> Starting function")  # Code executed before the original function
        func()  # Call the original function
        print(">>> Function finished")  # Code executed after the original function

    return wrapper


@simple_decorator
def greet():
    print("Hello, World!")


# Calling the decorated function
greet()
