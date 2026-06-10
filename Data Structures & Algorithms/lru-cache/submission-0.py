# implement a cache class with 2 functions get and put 
# init needs to initalize the LRU cache of size capacity
# -- basically the size of dict needs to be 2 
# get needs to get the key otherwise return -1
# put needs to update the value of the key of the key exists
# or add key-value pair 
# if new pair exceeds capacity, least recently used key needs to be removed so
# basically FIFO mechanism 
from collections import OrderedDict
# OrderedDict remembers insertion order and has
# move_to_end(key): move key to last position (most recently used)
# popitem(last=False): removes and returns the first (least recently used) item
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        # space: O(capacity), time: O(1)
        # case 1: return -1 since key doesnt exist 
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key) # mark as recently used
        # case 2: key exists in cache
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # case 1 update value of pair when key exists
        if key in self.cache:
            self.cache.move_to_end(key) # update order
        # case 2 add new key value pair / update
        self.cache[key] = value
        # case 3 if new added pair makes self.cache exceed capacity
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False) # remove LRU
