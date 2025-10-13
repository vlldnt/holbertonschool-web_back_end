#!/usr/bin/env python3
'''Most Recent Used Caching'''

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    '''Most Recent Used Class inherit from BaseCaching'''

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Most Recent Used caching'''
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru, _ = self.cache_data.popitem(last=True)
            print(f"DISCARD: {mru}")

        self.cache_data[key] = item

    def get(self, key):
        ''' get value from key '''
        if key is None or key not in self.cache_data:
            return None
        value = self.cache_data[key]
        self.cache_data.move_to_end(key, last=True)
        return value
