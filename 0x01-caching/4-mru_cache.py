#!/usr/bin/python3
""" MRU caching """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRU cache class """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = self.keys.pop()
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            self.keys.remove(key)
            self.keys.append(key)
        return self.cache_data.get(key, None)
