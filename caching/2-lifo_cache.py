#!/usr/bin/env python3
'''
Create a class FIFOCache that inherits from BaseCaching and is a caching system
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

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            firstOut = list(self.cache_data)[-1]
            print(f"DISCARD: {firstOut}")
            del self.cache_data[firstOut]

        self.cache_data[key] = item

    def get(self, key):
        ''' get value from key '''
        if key is None:
            return None
        return self.cache_data.get(key)
