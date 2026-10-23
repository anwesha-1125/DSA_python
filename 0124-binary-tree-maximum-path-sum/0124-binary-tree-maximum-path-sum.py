# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        self.ans = float('-inf')
        def getheight(root):
            if root is None:
                return 0
            left = max(0,getheight(root.left))
            right = max(0,getheight(root.right))
            self.ans = max(self.ans , left + right +root.val)
            return max(left,right) + root.val
        getheight(root)
        return self.ans
        