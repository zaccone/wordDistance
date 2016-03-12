class Dictionary(object):
    """Dictionary is a custom words dictionary.

    It extends standard Python dictionary where keys are in a form of
    morphed form of original words and values are sets of original words
    matching morphed ones.
    Example:

    Word ``dog`` will have 3 morphed values: '_og', 'd_g' and 'do_'.
    Dictionary object with one word will look as following:

    dictionary = {
        '_og': set(['dog']),
        'd_g': set(['dog']),
        'do_': set(['dog']),
    }

    Thanks to that it's relatively easy finding all corresponding words
    that are 'one letter' away.

    """

    def __init__(self):
        self._dictionary = {}

    def insert(self, word):
        """Insert word into a Dictionary object.

        For each morphed word assign original word.

        :param: word: Word to be inserted
        :type: string

        """
        for morphed_word in self.morph_word(word):
            wordset = self._dictionary.setdefault(morphed_word, set([]))
            wordset.add(word)

    def is_real_word(self, word):
        """Check if the word is in the dictionary.

        Instead of keeping set of original words see if original word is
        in values
        assigned to any of the morphed_word.

        :param word: Word to be checked
        :type: string
        :returns: False if word found in the dictionary, False otherwise
        """
        for morphed_word in self.morph_word(word):
            if (morphed_word not in self._dictionary or
                    word not in self._dictionary[morphed_word]):
                    return False
        return True

    def get_corresponding_words(self, word):
        """Get all words that have only one letter changed."

        Iterate over all 'morphed' words and return a set of values tied to
        each of the morphed value.

        :param word: starting word
        :returns: set of words 'one letter away' from asking word
        :rtype: set
        """
        result = set([])
        for morphed_word in self.morph_word(word):
            if self.is_real_word(word) is False:
                break
            for corresponding_word in self._dictionary[morphed_word]:
                result.add(corresponding_word)

        return result

    @staticmethod
    def morph_word(word):
        """Generate morphed combinations of the word
        Return a generator that for each letter replaces it with a wildcard '_'
        sign and yields new word to a caller.

        For word 'marek' values: _arek, m_rek, ma_ek, mar_k, mare_
        will be yielded.

        :param: word to be morphed
        :type: string

        :returns: a generator yielding morphed combinations
        :rtype: generator

        """
        for i in range(len(word)):
            yield word[0:i] + '_' + word[i+1:]

    @staticmethod
    def build(dict_file):
        """Build a dictionary from a file
        :param: dict_file: filename of the input filename
        :type: string

        :returns: Dictionary with populated words
        :rtype: Dictionary

        """
        def handleFile(self):
            try:
                with open(dict_file, 'r') as f:
                    for line in f:
                        yield line.lower().strip('\n\t')
            except IOError as e:
                raise SystemExit(e)

        d = Dictionary()

        words = handleFile(dict_file)
        for word in words:
            d.insert(word)

        return d
