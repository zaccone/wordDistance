import unittest

import dictionary
import graph


class GraphTests(unittest.TestCase):

    def setUp(self):
        self.dictionary = dictionary.Dictionary()
        self.dictionary.insert('marek')
        self.dictionary.insert('darek')
        self.dictionary.insert('cat')
        self.dictionary.insert('cot')
        self.dictionary.insert('cog')
        self.dictionary.insert('dog')
        self.graph = graph.Graph(self.dictionary)

    def test_one_distance_away_path(self):
        path = self.graph.bfs('marek', 'darek')
        self.assertListEqual(['marek', 'darek'], path)

    def test_two_distance_away_path(self):
        self.dictionary.insert('darem')

        path = self.graph.bfs('marek', 'darem')
        exp = ['marek', 'darek', 'darem']
        self.assertListEqual(exp, path)

    def test_path_symmetry(self):
        path = self.graph.bfs('cat', 'dog')
        rpath = self.graph.bfs('dog', 'cat')

        self.assertListEqual(path, rpath[::-1])

    def test_empty_path(self):
        path = self.graph.bfs('marek', 'dog')
        self.assertIsNone(path)

