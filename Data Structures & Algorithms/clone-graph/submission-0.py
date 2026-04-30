"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # dict mapping old --> new node to check if node has been cloned alr
        old_to_new = {node: Node(node.val)} 
        queue = deque([node])
        
        while queue:
            curr = queue.popleft()
            
            for neighbor in curr.neighbors:
                if neighbor not in old_to_new: # if neighbor not cloned alr,
                    # make a clone
                    old_to_new[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                old_to_new[curr].neighbors.append(old_to_new[neighbor]) # append cloned neighbor node to original cloned node
                # to the neighbors of the original node

        return old_to_new[node] # return start node