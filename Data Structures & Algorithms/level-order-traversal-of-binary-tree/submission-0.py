# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        res = []

        if root:
            queue.append(root)
            res.append([root.val])

        while len(queue) > 0:
            lvl = []

            for i in range(len(queue)):
                curr = queue.popleft()  # First in first out

                if curr.left is not None:
                    queue.append(curr.left)
                    lvl.append(curr.left.val)
                if curr.right is not None:
                    queue.append(curr.right)
                    lvl.append(curr.right.val)
            
            if len(lvl) > 0:
                res.append(lvl)
        
        return res