import sys

from sequenceTools import sequencePrint

if __name__ == '__main__':
    test_string = sys.stdin.read()
    sequencePrint.genBank_print(test_string)