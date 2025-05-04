class Solution:
    def maxSubArray(self, arr: list[int]) -> int:
        csum = arr[0]  # current sum
        osum = arr[0]  # overall sum
        
        for i in range(1, len(arr)):
            if csum > 0:
                csum += arr[i]
            else:
                csum = arr[i]
            
            if csum > osum:
                osum = csum
        
        return osum
