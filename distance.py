#!/usr/bin/python3

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


def main():
    dict_file, start_word, stop_word = parse()

    if len(start_word) != len(stop_word):
        print("Start and stop words differ in lengths, no common path")
        raise SystemExit(0)


    d = dictionary.Dictionary.build(dict_file)
    g = graph.Graph(d)
    path = g.bfs(start_word, stop_word)

    if path is None:
        print("There is no path between words {} and {}".format(
            start_word, stop_word))
    else:
        print("Path between words: {}".format("->".join(path)))

if __name__ == "__main__":
    main()
