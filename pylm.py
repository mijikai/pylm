#!/usr/bin/env python3


class PylmOneLine:
    def __ror__(self, other):
        yield from other.split('\n')

m = PylmOneLine()
