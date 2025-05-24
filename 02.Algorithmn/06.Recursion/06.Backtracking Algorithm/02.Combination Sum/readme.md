**Combination Sum**
Given an array of distinct integers arr[] and an integer target, 
the task is to find a list of all unique combinations of array where the sum of chosen element is equal to target.
Note: The same number may be chosen from array an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

Input: arr[] = [2, 4, 6, 8], target = 8
Output: [[2, 2, 2, 2], 
                [2, 2, 4],
                [2, 6],
                [4, 4],
                [8]]

Input: arr[] = [2, 7, 6, 5], target = 16
Output: [[2, 2, 2, 2, 2, 2, 2, 2],
                [2, 2, 2, 2, 2, 6],
                [2, 2, 2, 5, 5],
                [2, 2, 5, 7],
                [2, 2, 6, 6],
                [2, 7, 7],
                [5, 5, 6]]

**Step by step implementation**

To perform recursion, create an array cur[] to store the current combination and a 2D array res[] to store all valid combinations.
Start from the 0th element and for each element arr[i], there are two choices:
Include the element: Add it to array cur and reduce remSum by arr[i] and move to the same index as we can choose same element multiple times.
Skip the element: Move to the next element without adding the current.
If the remaining sum becomes 0, add the current combination cur to res else backtrack to previous element by removing the element from the last index of cur.



