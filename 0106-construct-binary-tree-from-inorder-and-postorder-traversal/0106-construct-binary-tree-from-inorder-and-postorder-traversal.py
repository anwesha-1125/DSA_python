# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        in_map = {val: idx for idx, val in enumerate(inorder)}

        def build(inStart, inEnd, postStart, postEnd):
            if inStart > inEnd or postStart > postEnd:
                return None

            # Root is the LAST element in postorder
            root_val = postorder[postEnd]
            root = TreeNode(root_val)

            # Find root in inorder
            inRoot = in_map[root_val]

            # Number of nodes in left subtree
            numsLeft = inRoot - inStart

            # Build left subtree
            root.left = build(
                inStart,
                inRoot - 1,
                postStart,
                postStart + numsLeft - 1
            )

            # Build right subtree
            root.right = build(
                inRoot + 1,
                inEnd,
                postStart + numsLeft,
                postEnd - 1
            )

            return root

        return build(
            0,
            len(inorder) - 1,
            0,
            len(postorder) - 1
        )