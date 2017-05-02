"""Read and print an integer series."""
import sys


def read_series(filename):
    """Read the series from a file."""
    try:
        f = open(filename, mode='rt', encoding='utf-8')
        return [int(line.strip()) for line in f]
    finally:
        f.close()


def main(filename):
    """Read the data from the file and print."""
    series = read_series(filename)
    print(series)


if __name__ == "__main__":
    main(sys.argv[1])
