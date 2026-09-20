# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:

        if root is None:
            return True
        def mirror(l,r):
            if l is None and r is None:
                return True
            if l is None or r is None:
                return False
            if l.val != r.val:
                return False
            return(mirror(l.left,r.right)and mirror(l.right,r.left))
        return mirror(root.left,root.right)



        # ans = []
        # def inorder(root):
        #     if root is None:
        #         ans.append(None)
        #         return
        #     inorder(root.left)
        #     ans.append(root.val)
        #     inorder(root.right)
        
        # inorder(root)
        # # print(ans)
        # n=len(ans)
        # mid = len(ans)//2 
        # def reverse(l,r):
        #     while l<r:
        #         ans[l],ans[r]=ans[r],ans[l]
        #         l+=1
        #         r-=1
        #     return ans
        # reverse(mid+1,n-1)
        # # print(ans)

        # p = 0
        # q = mid+1
        # while p <mid:
        #     if ans[p] == ans[q]:
        #         p+=1
        #         q+=1
        #     else:
        #         return False
        # return True