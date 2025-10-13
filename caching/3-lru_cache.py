#!/usr/bin/env python3
'''Last Recent Used Caching'''


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        '''Last Recent Used caching'''
        if key is None or item is None:
            return

        if key in self.cache_data:
            del self.cache_data[key]
            self.cache_data[key] = item
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru = list(self.cache_data)[0]
            print(f"DISCARD: {lru}")
            del self.cache_data[lru]

        self.cache_data[key] = item

    def get(self, key):
        """Return value and mark as recently used"""
        if key is None:
            return None
        value = self.cache_data.get(key)
        if value is None:
            return None
        del self.cache_data[key]
        self.cache_data[key] = value
        return value
