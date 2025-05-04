'''Given a Linked List A consisting of N nodes.

The Linked List is binary i.e data values in the linked list nodes consist of only 0's and 1's.

You need to sort the linked list and return the new linked list.'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def solve(self, A: ListNode) -> ListNode:
        if A is None or A.next is None:
            return A
        
        count = A
        curr = A
        
        while curr is not None:
            if curr.val != 1:
                curr.val, count.val = count.val, curr.val
                count = count.next
            curr = curr.next
        
        return A
