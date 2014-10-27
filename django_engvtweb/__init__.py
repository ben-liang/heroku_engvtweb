import os

# Ensure path is correct
PARENT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.path.pardir))


def repository_path(*paths):
    """Returns an absolute path relative to this repository

    :param paths: extra path elements relative to the repository, via
        :func:os.path.join

    :returns: absolute path reference
    :rtype: str
    """
    return os.path.abspath(os.path.join(PARENT_DIR, *paths))

