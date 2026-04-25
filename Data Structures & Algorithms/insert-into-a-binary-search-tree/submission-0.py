# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # binary tree rule: root.right.val has to be larger than root.val, 
        # root.left.val has to be smaller than root.val 

        # for recursion, we need a base case
        # create a node with that value if the node doesnt exist 
        if not root:
            return TreeNode(val)

        # return the root node
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        elif val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            return root
        
        return root