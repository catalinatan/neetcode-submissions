# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMinNode(self,curr):
        # keep going left since left of binary tree is smaller
        if not curr:
            return None

        while curr and curr.left:
            curr = curr.left
            
        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # if key == root.val
        else:
            # 2 main conditions

            # 1) remove a node with either 0/1 child
            if not root.left:
                root = root.right # replace current root with the one thats not null 
            elif not root.right:
                root = root.left
            # 2) remove a node with 2 children 
            else:
                # find the min node from right subtree
                minNode = self.findMinNode(root.right)
                root.val = minNode.val
                # remove duplicate original min node
                root.right = self.deleteNode(root.right, minNode.val)
        return root
            
            

