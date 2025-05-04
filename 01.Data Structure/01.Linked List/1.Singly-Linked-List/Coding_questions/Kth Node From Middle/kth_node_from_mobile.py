#kth node implementation in python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def solve(self, A: ListNode, B: int) -> int:
        t = A
        n = 0
        
        # Count the number of nodes in the list
        while t is not None:
            n += 1
            t = t.next
        
        mn = (n // 2) + 1
        t = A
        nd = mn - B
        
        if nd < 1:
            return -1
        else:
            for i in range(1, nd):
                t = t.next
            return t.val
