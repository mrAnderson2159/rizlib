from collections import Callable


def confirm(prompt: str, color: Callable = lambda s: s) -> bool:
    """Takes a prompt to be shown to the user,
    expects user's input and returns whether the answer is 'y' (positive) or not

    :param prompt: a query message lacking of the question mark
    :param color: [optional] a c_[color] function from rizlib.terminal.text.color
    :return: if user entered 'y' ignore case
    """
    return input(color(str.capitalize(prompt) + '? (y/n): ')) in ('y', 'Y')
