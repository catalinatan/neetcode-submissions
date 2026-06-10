# use hash map to find a node by its key O(1) 
# double linked list to move nodes to most recently used position and 
# remove the least recenty used node from other end in O(1)
# assumptions: least is on the left, most is o the right
# double linked list means both directions can travel 
# needs to have left dummy before LRU and right dummy after MRU 
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val 
        # self.prev points to node before it, 
        # self.next points to the node after it
        # both set to None for initialization
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.left, self.right = Node(0, 0), Node(0, 0)
        # connect nodes to each other both directions
        self.left.next, self.right.prev = self.right, self.left

    # add helper functions 
    # 1) remove(node) 
    # unlink node from the list by connecting its prev and next nodes 
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # 2) insert(node)
    # insert node just before right (mark as most recently used)
    def insert(self,node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # need to remove then insert so it marks as recently used
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        # if key not in cache 
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
