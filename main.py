import sys

from sequenceTools import sequencePrint

if __name__ == '__main__':
    test_string = sys.stdin.read()
    print(' '.join(sequencePrint.string_to_blocks(test_string, 10)))