"""Reading the contents of a file."""
import sys


def main(filename):
    """Read the contents of the file."""
    f = open(filename, mode='rt', encoding='utf-8')
    for line in f:
        print(line, end='')
    f.close()


if __name__ == "__main__":
    main(sys.argv[1])
