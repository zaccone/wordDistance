import collections


class Path(object):
    """Path object represents a single node in a words path
    It's used for finding path between two corresponding words.
    Technically it is a reversed linked list where each node keeps a value set to a
    certain word and a pointer to the previous node.

    """
    def __init__(self, word, previous=None):
        self.word = word
        self.previous = previous

    def get_path(self):
        """Generate path starting from this path."""
        node = self
        result = collections.deque()
        while node is not None:
            result.appendleft(node.word)
            node = node.previous

        return list(result)
