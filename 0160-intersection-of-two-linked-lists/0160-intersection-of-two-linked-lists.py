# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp = headA
        temp1 = headA
        temp2 = headB
        cnt1 = 0
        cnt2 = 0
        while temp is not None:
            cnt1 += 1
            temp = temp.next
        temp = headB
        while temp is not None:
            cnt2 += 1
            temp = temp.next
        if cnt1 > cnt2:
            diff = cnt1 - cnt2
            for i in range(diff):
                temp1 = temp1.next
        else:
            diff = cnt2 - cnt1
            for i in range(diff):
                temp2 = temp2.next
        while temp1 != temp2:
            temp1 = temp1.next
            temp2 = temp2.next
        return temp1
        