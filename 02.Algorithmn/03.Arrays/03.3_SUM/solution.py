from typing import List

class Solution:
    def twoSum(self, arr: List[int], target: int, si: int, ei: int) -> List[List[int]]:
        ans = []
        while si < ei:
            sum_val = arr[si] + arr[ei]
            if sum_val == target:
                small_ans = [arr[si], arr[ei]]
                ans.append(small_ans)
                si += 1
                ei -= 1
                while si < ei and arr[si] == arr[si - 1]:
                    si += 1
                while si < ei and arr[ei] == arr[ei + 1]:
                    ei -= 1
            elif sum_val < target:
                si += 1
            else:
                ei -= 1
        return ans

    def prepareAns(self, ans: List[List[int]], small_ans: List[List[int]], fix_ele: int):
        for arr in small_ans:
            ar = [fix_ele] + arr
            ans.append(ar)

    def threeSum(self, arr: List[int], target: int, si: int, ei: int) -> List[List[int]]:
        ans = []
        arr.sort()
        i = si
        while i < ei:
            small_ans = self.twoSum(arr, target - arr[i], i + 1, ei)
            self.prepareAns(ans, small_ans, arr[i])
            i += 1
            while i < ei and arr[i] == arr[i - 1]:
                i += 1
        return ans

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return self.threeSum(nums, 0, 0, len(nums) - 1)
