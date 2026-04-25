# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            # return height of the root, if the subtree has no children its height is 0 
            if not root:
                return 0

            # height from non-empty subtree comes from their children
            left = dfs(root.left)
            right = dfs(root.right)
        
            if abs(left - right) > 1 or left == -1 or right == -1: 
                return -1
            else:
                height = 1 + max(left,right) 
                return height

        return False if dfs(root) < 0 else True

        # if not left_subtree or not right_subtree:
        #     return False
        # else:
        #     return True
        


        

