#!/usr/bin/python

import sys

import dictionary
import graph


def parse():
    try:
        dict_file, start_word, stop_word = sys.argv[1:5]
        return (dict_file, start_word, stop_word)
    except (IndexError, ValueError):
        msg = "Usage: {} /path/to/dict startWord stopWord".format(
                sys.argv[0])
        print(msg)
        raise(SystemExit(-1))


def check_word_lengths(start_word, stop_word):
    """Check if the both words are of equal length.

    :param start_word: Starting word
    :param stop_word: Stopping word
    :returns: True if lengths are equal, False otherwise
    :rtype: bool

    """
    if len(start_word) != len(stop_word):
        print("Words {} and {} are of different length".format(
            start_word, stop_word))
        return False
    return True


def check_words(dictionary_, start_word, stop_word):
    """Check if both words are defined in the dictionary.__doc__

    If either word is not found, an appropriate warning will be printed
    to stdout

    :param dictionary_ : dictionary object
    :type: Dictionary
    :param start_word: Starting word
    :type: string
    :param stop_word: Stopping word
    :type: string
    :returns: True if both words are defined, False othwerise
    :rtype: bool

    """
    if dictionary_.is_real_word(start_word) is False:
        print("Word {} not found in the dictionary".format(start_word))
        return False
    if dictionary_.is_real_word(stop_word) is False:
        print("Word {} not found in the dictionary".format(stop_word))
        return False
    return True


def main():
    dict_file, start_word, stop_word = parse()

    if check_word_lengths(start_word, stop_word) is False:
        raise SystemExit(0)

    d = dictionary.Dictionary.build(dict_file)
    if check_words(d, start_word, stop_word) is False:
        raise SystemExit(0)

    g = graph.Graph(d)
    path = g.bfs(start_word, stop_word)

    if path is None:
        print("There is no path between words {} and {}".format(
            start_word, stop_word))
    else:
        print("One possible path between words: {}".format("->".join(path)))

if __name__ == "__main__":
    main()
