#!/usr/bin/env python
import sys


def get_names(filename):
    names = []
    with open(filename) as f:
        for line in f:
            names.append(line.strip())
    return names


def write_initials(names, filename):
    initials = [name[0] for name in names]
    with open(filename, 'w') as f:
        f.writelines('\n'.join(initials))


def main():
    if len(sys.argv) != 3:
        print('usage: {} filename_in filename_out'.format(sys.argv[0]))
        sys.exit(1)

    filename_in = sys.argv[1]
    filename_out = sys.argv[2]
    names = get_names(filename_in)
    write_initials(names, filename_out)


if __name__ == '__main__':
    main()
