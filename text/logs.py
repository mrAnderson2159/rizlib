"""
Contains the definitions of functions used to print colored logs to the terminal screen.

Example:
    success("file loaded") prints the string "SUCCESS: file loaded" colored in green
    warning("task skipped") prints the string "WARNING: task skipped" colored in yellow

It also contains an enum class called Silence, used to silence warnings.

Example:
    def foo(*args, silence):
        # task 1
        success(msg, silence)
        # task 2
        warning(msg, silence)
        # task 3
        success(msg, silence)

    foo(*args, Silence.success) will only print a warning
"""

__all__ = {'Silence', 'success', 'warning'}
__author__ = "Valerio Molinari"
__credits__ = "Valerio Molinari"
__maintainer__ = "Valerio Molinari"
__email__ = "valeriomolinariprogrammazione@gmail.com"

from typing import Callable

from text.colors import yellow, green
from enum import Enum, auto


class Silence(Enum):
    """Used to silence logs"""
    none = auto()
    success = auto()
    warning = auto()
    all = auto()


def __silenced_by(silence: Silence):
    """A decorator to tell log functions what Silence enum disable them

    :param silence: logs.Success enum class value
    """

    def function_wrapper(function: Callable[[str, Silence], None]):
        def wrap(message: str, silencer: Silence = Silence.none):
            if silencer not in (silence, Silence.all):
                function(message, None)

        wrap.__doc__ = function.__doc__
        wrap.__name__ = function.__name__
        return wrap

    return function_wrapper


def __set_doc__(function: Callable, color: str):
    name = function.__name__
    function.__doc__ = f"""Prints "{name.upper()}: message" colored in {color}
    
    :param message: the message to be print on the screen
    :param silence: a log.Silence enum value which, when equal to Silence.{name} disables
    this log
    """


@__silenced_by(Silence.success)
def success(message: str, silence: Silence = Silence.none):
    green(f"SUCCESS: {message}")


@__silenced_by(Silence.warning)
def warning(message: str, silence: Silence = Silence.none):
    yellow(f'WARNING: {message}')


__set_doc__(success, 'green')
__set_doc__(warning, 'yellow')
