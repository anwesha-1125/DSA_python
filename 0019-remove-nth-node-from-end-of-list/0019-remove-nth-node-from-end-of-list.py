# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        s = f = head
        while n:
            f = f.next
            n -= 1
        if f is None:
            return head.next
        while f != None and f.next != None:
            s = s.next
            f = f.next
        
        s.next = s.next.next
        return head