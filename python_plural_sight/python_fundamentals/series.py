"""Read and print an integer series."""
import sys


def read_series(filename):
    """Read the series from a file."""
    with open(filename, mode='rt', encoding='utf-8') as f:
        return [int(line.strip()) for line in f]


def main(filename):
    """Read the data from the file and print."""
    series = read_series(filename)
    print(series)


if __name__ == "__main__":
    main(sys.argv[1])
