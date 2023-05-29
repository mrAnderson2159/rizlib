from typing import Callable


def copy_func_attrs_in_wrapper(wrapper: Callable, function: Callable):
    """Used to copy dunder attributes of a function inside its wrapper
    in order to make the wrapper emulate the function

    :param wrapper: the wrapper inside the decorator
    :param function: the function called inside the wrapper
    """
    attrs = ['__name__', '__doc__']
    for attr in attrs:
        setattr(wrapper, attr, getattr(function, attr))
