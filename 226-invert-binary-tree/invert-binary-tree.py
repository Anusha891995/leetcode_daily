# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        
        # 1. Swap the left and right children
        # This is like saying: Left becomes Right, and Right becomes Left
        root.left, root.right = root.right, root.left
        
        # 2. Recursively call the function on the new children
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # 3. Return the root of the now-inverted tree
        return root