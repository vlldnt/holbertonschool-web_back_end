#!/usr/bin/env python3
'''Add and GET LFU Caching'''
from base_caching import BaseCaching

class LFUCache(BaseCaching):
    """Least Frequently Used Cache"""

    def __init__(self):
        '''Init from base model'''
        super().__init__()
        self.usage_count = {}

    def put(self, key, item):
        '''Put LFU cachin algo'''
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_count[key] += 1
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            min_count = min(self.usage_count.values())
            lfu_keys = [k for k, v in self.usage_count.items() if v == min_count]
            lfu_key = lfu_keys[0]
            print(f"DISCARD: {lfu_key}")
            del self.cache_data[lfu_key]
            del self.usage_count[lfu_key]

        self.cache_data[key] = item
        self.usage_count[key] = 1

    def get(self, key):
        '''GET LFU cachin algo'''
        if key is None or key not in self.cache_data:
            return None

        self.usage_count[key] += 1
        return self.cache_data[key]
