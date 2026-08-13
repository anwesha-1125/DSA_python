# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        leftheight = self.getheight(root.left)
        rightheight = self.getheight(root.right)
        if abs(leftheight - rightheight) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False

    def getheight(self,root):
        if root is None:
            return 0
        leftheight = self.getheight(root.left)
        rightheight = self.getheight(root.right)
        return max(leftheight,rightheight)+1

        