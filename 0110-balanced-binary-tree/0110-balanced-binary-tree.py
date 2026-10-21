# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        if root is None:
            return True
        lefth = self.getheight(root.left)
        righth = self.getheight(root.right)
        if abs(lefth-righth)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False
    def getheight(self,root):
        if root is None:
            return 0
        left = self.getheight(root.left)
        right = self.getheight(root.right)
        return max(left,right)+1
        