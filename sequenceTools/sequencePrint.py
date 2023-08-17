"""
utilities for printing sequence strings
"""


def string_to_blocks(string, block_length=3):
    """
    Split a string into blocks of length block_length
    :param string: Input
    :param block_length: length to split into
    :return: list of strings of block length
    """

    return [
        string[ind:ind+block_length] for ind in range(0, len(string), block_length)
    ]
