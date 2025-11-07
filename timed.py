import time


def timer_decorator(func):
    """
    A decorator that measures the execution time of a function.
    """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(
            f"Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds."
        )
        return result

    return wrapper


@timer_decorator
def long_running_function(n):
    """
    A sample function that simulates a long-running task.
    """
    sum_val = 0
    for i in range(n):
        sum_val += i
    return sum_val


@timer_decorator
def another_function(a, b):
    """
    Another sample function to demonstrate decorator usage.
    """
    time.sleep(0.5)  # Simulate some work
    return a + b


# Call the decorated functions
long_running_function(10000000)
result = another_function(5, 7)
print(f"Result of another_function: {result}")
