"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # make a pointer to the head of the current list 
        # while there is still a next where it isnt null basically 
        # try to make the pointer point to the next node and the current pointers random to the 
        # random node 
        # then iterate to the next node

        # can use hashtable for key would be the order of the node then 
        # val can be [value, random_node]
        if not head:
            return None

        hashmap = {}
        curr = head 

        # first pass
        while curr:
            hashmap[curr] = Node(curr.val)
            curr = curr.next 

        hashmap[None] = None
      
        # second pass:
        dummy = head 
        while dummy:
            new_node = hashmap[dummy]
            copy_node_next = hashmap[dummy.next]
            new_node.next = copy_node_next

            copy_random_node = hashmap[dummy.random]
            new_node.random = copy_random_node
            dummy = dummy.next

        return hashmap[head]
    
       



