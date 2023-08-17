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

def genBank_print(string, block_length=10, block_no=6):
    """
    Display genetic sequence in GenBank style
    :param string:
    :param block_length:
    :param block_no:
    :return:
    """
    #break into a list of lines
    line_list = string_to_blocks(string, block_length*block_no)
    #define a counter to add the base number to the start of each line
    base_number = 1
    base_number_space = 5 #the size of the column which contains the base number
    #break each line into blocks and print
    for line in line_list:
        print (str(base_number).rjust(base_number_space)," ".join(string_to_blocks(line, block_length)).lower())
        base_number += block_length*block_no
    return

