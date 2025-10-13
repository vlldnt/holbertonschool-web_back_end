#!/usr/bin/env python3
'''
Create a class LIFOCache that inherits from BaseCaching and is a caching system
'''

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''Class LIFO Cache inherit from BAse Caching'''
    def __init__(self):
        '''Super init'''
        super().__init__()

    def put(self, key, item):
        '''Add a new key with item, Last_In First_Out'''
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data)[-1]
            print(f"DISCARD: {last_key}")
            del self.cache_data[last_key]

        self.cache_data[key] = item

    def get(self, key):
        ''' get value from key '''
        if key is None:
            return None
        return self.cache_data.get(key)
