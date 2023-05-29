import time
from typing import Callable, Any
from rizlib.tools.decorators import copy_func_attrs_in_wrapper


def speed_test(function: Callable) -> Callable:
    """A decorator used to calculate the time execution of a function.
    Returns a 2-tuple with the return value of the function and the elapsed time.

    :param function: the decorated function
    :return: a tuple with the value returned by the function and the elapsed type
    """
    def wrapper(*args, **kwargs) -> tuple[Any, float]:
        t = time.time()
        f = function(*args, **kwargs)
        return f, time.time() - t

    copy_func_attrs_in_wrapper(wrapper, function)
    return wrapper


if __name__ == '__main__':
    @speed_test
    def add(a: int, b: int) -> int:
        """Sum two integers

        :param a: first int
        :param b: second int
        :return: sum of a and b
        """
        return a + b

    print(add(3, 5))