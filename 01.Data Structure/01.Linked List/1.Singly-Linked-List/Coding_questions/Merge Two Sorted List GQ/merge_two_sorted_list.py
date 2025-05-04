#Code to merge two sorted list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, h1: ListNode, h2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        p1 = h1
        p2 = h2
        p3 = dummy
        
        while p1 is not None and p2 is not None:
            if p1.val < p2.val:
                p3.next = p1
                p1 = p1.next
            else:
                p3.next = p2
                p2 = p2.next
            p3 = p3.next
        
        while p1 is not None:
            p3.next = p1
            p1 = p1.next
            p3 = p3.next
        
        while p2 is not None:
            p3.next = p2
            p2 = p2.next
            p3 = p3.next
        
        return dummy.next
