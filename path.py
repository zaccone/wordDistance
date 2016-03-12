import collections

class Path(object):
    def __init__(self, word, previous = None):
        self.word = word
        self.previous = previous
    def get_path(self):
        node = self
        result = collections.deque()
        while node:
            result.appendleft(node.word)
            node = node.previous

        return list(result)
