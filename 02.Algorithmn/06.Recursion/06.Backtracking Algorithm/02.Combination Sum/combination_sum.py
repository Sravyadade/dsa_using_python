# Python program to find all combinations that
# sum to a given target

# Function to generate all combinations
# of arr that sums to target.
def makeCombination(arr, remSum, cur, res, index):

    # If remSum is 0 then add the combination to the result
    if remSum == 0:
        res.append(list(cur))
        return

    # Invalid Case: If remSum is less than 0 or if index >= len(arr)
    if remSum < 0 or index >= len(arr):
        return

    # Add the current element to the combination
    cur.append(arr[index])

    # Recur with the same index
    makeCombination(arr, remSum - arr[index], cur, res, index)

    # Remove the current element from the combination
    cur.pop()

    # Recur with the next index
    makeCombination(arr, remSum, cur, res, index + 1)

# Function to find all combinations of elements
# in array arr that sum to target.
def combinationSum(arr, target):
    arr.sort()

    # List to store combinations
    cur = []

    # List to store valid combinations
    res = []
    makeCombination(arr, target, cur, res, 0)
    
    return res

if __name__ == "__main__":
    arr = [2, 4, 6, 8]
    target = 8

    res = combinationSum(arr, target)

    for v in res:
        print(" ".join(map(str, v)))
