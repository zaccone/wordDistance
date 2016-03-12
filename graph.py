import path


class Graph(object):
    """Graph is a graph object operating on Dictionary object."""
    def __init__(self, dictionary):
        """Graph maintains three internal data structures.

        1) visited with words already visited.
        2) _dictionary: instance of Dictionary object
        3) word_to_path: dictionary (in Python sense) where each word is
        a key and maitains chain of Path objects to the first word.

        """
        self.visited = set([])
        self._dictionary = dictionary
        self.word_to_path = {}

    def bfs(self, start_word, stop_word):
        """Implementation of Binary Search Tree.
        :param start_word: Starting word
        :param stop_word: Stopping word
        :returns path between start and stop words, None if not found.
        :rtype: list or None

        """
        q = []
        q.append(start_word)
        self.visited.add(start_word)
        node = path.Path(start_word, None)
        self.word_to_path[start_word] = node

        while q:
            word = q.pop(0)

            node = self.word_to_path[word]
            if word == stop_word:
                return node.get_path()

            words_distance_awa = self._dictionary.get_corresponding_words(word)

            words_distance_awa = words_distance_awa - self.visited
            self.visited.update(words_distance_awa)

            for word in words_distance_awa:
                self.word_to_path[word] = path.Path(word, node)

            q.extend(list(words_distance_awa))
        return None
