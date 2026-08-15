# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def distanceK(self, root, target, k):

        parent = {}

        def make_parent(node, par=None):
            if not node:
                return

            parent[node] = par

            make_parent(node.left, node)
            make_parent(node.right, node)

        make_parent(root)

        # Step 2: BFS from target
        q = deque([target])
        visited = {target}
        distance = 0

        while q:
            size = len(q)

            if distance == k:
                return [node.val for node in q]

            for _ in range(size):
                node = q.popleft()

                # Go left
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    q.append(node.left)

                # Go right
                if node.right and node.right not in visited:
                    visited.add(node.right)
                    q.append(node.right)

                # Go to parent
                if parent[node] and parent[node] not in visited:
                    visited.add(parent[node])
                    q.append(parent[node])

            distance += 1

        return [] 