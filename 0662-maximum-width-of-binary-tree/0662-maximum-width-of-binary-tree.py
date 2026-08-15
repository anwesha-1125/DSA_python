# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        ans = 0
        q = deque([(root,0)])
        while q:
            size = len(q)
            first = q[0][1]
            for _ in range(size):
                node,index = q.popleft()
                if node.left:
                    q.append((node.left, 2 * index + 1))
                if node.right:
                    q.append((node.right, 2 * index + 2))
            last = index
            ans = max(ans, last - first + 1)
        return ans
                        