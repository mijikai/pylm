#!/usr/bin/env python3
import operator


class PylmOneLine:
    def __init__(self, func=None):
        self._func = func

    def __ror__(self, other):
        res = other.split('\n')
        if self._func is None:
            yield from res
        else:
            yield from map(self._func, res)

    def __getitem__(self, index):
        return PylmOneLine(lambda line: line[index])

m = PylmOneLine()
