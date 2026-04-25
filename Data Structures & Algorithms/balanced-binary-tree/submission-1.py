# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            # Return 2-place list
            if not root:
                # boolean for balanced/not balanced, and height
                return [True, 0] # empty tree has a height of node

            left = dfs(root.left)
            right = dfs(root.right)

            # if left and right node are both balanced 
            # and the height of the tree is balanced
            # then it should be balanced else
            # it's definitely not balanced
            balanced = (left[0] and right[0] and abs(right[1] - left[1]) <= 1) # height is in index 1 
            
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]


