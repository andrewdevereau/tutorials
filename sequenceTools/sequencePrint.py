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

def genBank_print(string, block_length=10, block_no=6, case='lower'):
    """
    Display genetic sequence in GenBank style
    :param string:
    :param block_length:
    :param block_no:
    :return:
    """
    # first change case of string if necessary
    if case == 'lower':
        string = string.lower()
    elif case == 'upper':
        string = string.upper()

    # break into a list of lines
    line_list = string_to_blocks(string, block_length*block_no)

    # define a counter to add the base number to the start of each line
    base_number = 1
    base_number_space = 5 # the width of the column which contains the base number
    gap_width = 1   #the size of the gap between columns
    col_gap = " "*gap_width  #define the column gap string
    # break each line into blocks and print
    for line in line_list:
        print (str(base_number).rjust(base_number_space),col_gap.join(string_to_blocks(line, block_length)))
        base_number += block_length*block_no  #update the base number by adding the number of bases in a line
    return

