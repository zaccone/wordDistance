class Dictionary(object):
    def __init__(self):
        self._dictionary = {}

    def insert(self, word):
        for morphed_word in self.morph_word(word):
            wordset = self._dictionary.setdefault(morphed_word, set([]))
            wordset.add(word)

    def get_corresponding_words(self, word):
        result = set([])
        for morphed_word in self.morph_word(word):
            for corresponding_word in self._dictionary[morphed_word]:
                result.add(corresponding_word)
        return result

    @staticmethod
    def morph_word(word):
        for i in range(len(word)):
            yield word[0:i] + '_' + word[i+1:]

    @staticmethod
    def build(dict_file):
        def handleFile(self):
            try:
                with open(dict_file, 'r') as f:
                    for line in f:
                        yield line
            except IOError as e:
                raise SystemExit(e)

        d = Dictionary()

        words = handleFile(dict_file)
        for word in words:
            d.insert(word)

        return d