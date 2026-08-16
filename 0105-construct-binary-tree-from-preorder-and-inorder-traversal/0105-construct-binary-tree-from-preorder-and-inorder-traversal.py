# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_map = {val: idx for idx, val in enumerate(inorder)}

        # Helper function to build tree recursively
        def build(preStart, preEnd, inStart, inEnd):
            if preStart > preEnd or inStart > inEnd:
                return None

            # Root from preorder
            root_val = preorder[preStart]
            root = TreeNode(root_val)

            # Find index in inorder
            inRoot = in_map[root_val]
            numsLeft = inRoot - inStart

            # Recurse on left and right
            root.left = build(
                preStart + 1,
                preStart + numsLeft,
                inStart,
                inRoot - 1
            )

            root.right = build(
                preStart + numsLeft + 1,
                preEnd,
                inRoot + 1,
                inEnd
            )

            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)