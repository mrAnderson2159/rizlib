from typing import Iterable, Iterator


def human_join(sequence: Iterable, conjunction: str = 'and'):
    """An enhancement of the str.join function. Allows to join a sequence of strings
    of numbers in a more human way.

    Example:
        >>> fruits = ['apples', 'strawberries', 'cherries']
        >>> human_join(fruits)
        >>> "apples, strawberries and cherries"

    :param sequence: a sequence of strings or number (or whatever object implementing a __str__
    method
    :param conjunction: a word to join the first elements with the last one, "and" by default
    :return: the joined sequence of elements
    """
    sequence = tuple(sequence)
    first_elements, last_element = sequence[:-1], sequence[-1]
    conjunction = f" {conjunction.strip()} "
    return ','.join(first_elements) + conjunction + last_element


def indent_lines(text: str, indentation: int) -> str:
    """Takes a multiline text and add indents each line by "indentation" value

    :param text: a multiline text
    :param indentation: number of '\t' to add before each line
    :return: indented text
    """
    return '\n'.join(map(lambda line: '\t' * indentation + line, text.split('\n')))


def spaced(sequence: list[str], extraspace: int = 0, after: bool = True) -> Iterator[str]:
    """Takes a list of strings, calculates the longest and adds spaces before or after the other
    strings to get the same length as the longest.

    Example:
        >>> hobbies = ['videogames', 'reading', 'birdwatching', 'jogging']
        >>> print(' '.join(spaced(hobbies)))
        videogames   reading      birdwatching jogging
        >>> print(' '.join(spaced(hobbies, extraspace=5)))
        videogames        reading           birdwatching      jogging
        >>> print(' '.join(spaced(hobbies, extraspace=5, after=False)))
               videogames           reading      birdwatching           jogging


    :param sequence: a sequence of strings
    :param extraspace: [optional] add a further number of spaces to each string
    :param after: [optional] a boolean to indicate if spaces must be added before or after
    the strings, True by default
    :return: An iterator of strings where every strings as the same length as sum of
    characters and spaces
    """
    def add_spaces(string, spaces):
        nonlocal after
        str_spaces = ' ' * spaces
        return string + str_spaces if after else str_spaces + string

    max_len = max(map(len, sequence))
    spaces_sequence = map(lambda s: max_len - len(s) + extraspace, sequence)
    return map(lambda zipped: add_spaces(*zipped), zip(sequence, spaces_sequence))


if __name__ == '__main__':
    hobbies = ['birdwatching', 'videogames', 'reading', 'jogging']
    print(' '.join(spaced(hobbies, extraspace=5)))

    for hobby in spaced(hobbies, after=False):
        print(hobby)

