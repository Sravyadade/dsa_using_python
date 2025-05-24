# Python program for activity selection problem
# when input activities may not be sorted.

# Function to solve the activity selection problem
def activitySelection(start, finish):

    # to store results.
    ans = 0

    # to store the activities
    arr = []

    for i in range(len(start)):
        arr.append((finish[i], start[i]))

    # sort the activities based on finish time
    arr.sort()

    # to store the end time of last activity
    finishtime = -1

    for i in range(len(arr)):
        activity = arr[i]
        if activity[1] > finishtime:
            finishtime = activity[0]
            ans += 1

    return ans


if __name__ == "__main__":
    start = [1, 3, 0, 5, 8, 5]
    finish = [2, 4, 6, 7, 9, 9]
    print(activitySelection(start, finish))
