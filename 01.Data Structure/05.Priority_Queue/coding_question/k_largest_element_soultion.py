# find the kth largest element solution in python
import heapq
class Solution:
    def kLargest(self, a, n, k):
        pq = []
        for i in range(n):
            if i < k:
                heapq.heappush(pq, a[i])
            else:
                if pq[0] < a[i]:
                    heapq.heappop(pq)
                    heapq.heappush(pq, a[i])
        
        ans = sorted(pq, reverse=True)
        return ans
