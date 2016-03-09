#!/usr/bin/python3

import sys

import dictionary


def parse():
    try:
        dict_file, start_word, stop_word = sys.argv[1:5]
        return (dict_file, start_word, stop_word)
    except (IndexError, ValueError):
        msg = "Usage: {} /path/to/dict startWord stopWord".format(
                sys.argv[0])
        print(msg)
        raise(SystemExit(-1))


def main():
    dict_file, start_word, stop_word = parse()
    d = dictionary.Dictionary.build(dict_file)
    import pdb
    pdb.set_trace()


if __name__ == "__main__":
    main()
