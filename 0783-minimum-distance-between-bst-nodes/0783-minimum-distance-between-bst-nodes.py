# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode | None) -> int:
        ans = []
        def inorder(root):
            if root is None:
                return None
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
        inorder(root)

        l = 0
        mini = float('inf')
        for i in range(1,len(ans)):
            diff = ans[i] - ans[i-1]
            mini = min(mini,diff)
        return mini