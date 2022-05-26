from collections.abc import Iterator
class wrapper_hasNext(Iterator):
    def __init__(self, it):
        self.it = iter(it)
        self._hasNext = None

    def __iter__(self):
        return self

    def __next__(self):
        if self._hasNext:
            result = self._thenext
        else:
            result = next(self.it)
        self._hasNext = None
        return result

    def hasNext(self):
        if self._hasNext is None:
            try:
                self._thenext = next(self.it)
            except StopIteration:
                self._hasNext = False
            else: self._hasNext = True
        return self._hasNext