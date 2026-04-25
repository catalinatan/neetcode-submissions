# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Use BFS, for each level find if theres a node on the left, if not then u need to find the most 
        # right node of the BST
        res = []
        # last in first out in each level ? the last in is the most right node

        q = deque()

        if root:
            q.append(root)
            res.append(root.val)
        
        lvl_no = 0 
        while len(q) > 0: 
            lvl = []
            for i in range(len(q)):
                curr = q.popleft()

                if curr:
                    lvl.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
            
            if lvl and lvl_no >= 1:
                res.append(lvl[-1])
        
            lvl_no += 1 

        return res