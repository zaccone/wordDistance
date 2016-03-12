import path


class Graph(object):
    def __init__(self, dictionary):
        self.visited = set([])
        self._dictionary = dictionary
        self.word_to_path = {}

    def bfs(self, start_word, stop_word):
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
