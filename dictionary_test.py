import unittest

import dictionary


class DictionaryTests(unittest.TestCase):

    def setUp(self):
        self.dictionary = dictionary.Dictionary()

    def test_word_morphing(self):

        word = 'marek'
        expected = ['_arek', 'm_rek', 'ma_ek', 'mar_k', 'mare_']
        morphed_words = dictionary.Dictionary.morph_word(word)
        self.assertListEqual(expected, list(morphed_words))

    def test_empty_word_morphing(self):

        word = ''
        expected = []

        morphed_words = dictionary.Dictionary.morph_word(word)
        self.assertListEqual(expected, list(morphed_words))

    def test_neigbours(self):
        words = ['marek', 'darek', 'jarek']
        for word in words:
            self.dictionary.insert(word)

        neighbours = self.dictionary.get_corresponding_words('marek')
        self.assertEqual(set(words), neighbours)

    def test_neighbours_non_connected_words(self):
        words1 = ['marek', 'jarek', 'darek']
        words2 = ['kotek', 'motek']
        for word in words1:
            self.dictionary.insert(word)

        for word in words2:
            self.dictionary.insert(word)

        neighbours = self.dictionary.get_corresponding_words('marek')
        self.assertEqual(set(words1), set(neighbours))
