from pathlib import Path


def get_parent_dir(file: str, with_slash: bool = True) -> str:
    """Returns the path to the parent dir of a file

    :param file: path to the file
    :param with_slash: (optional) to add the slash character at the end of the path (default = False)
    :return: the path to file's parent dir
    """
    return str(Path(file).parent.resolve()) + ('/' if with_slash else '')


