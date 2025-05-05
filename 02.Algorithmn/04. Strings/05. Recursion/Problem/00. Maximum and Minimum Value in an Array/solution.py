def main():
    arr = [12, 43, 45, 23, -420, -8, 69, 67, 1]
    n = len(arr)
    print("Minimum Element of Array:", get_min(arr, 0, n))
    print("Maximum Element of Array:", get_max(arr, 0, n))

def get_min(arr, i, n):
    if n == 1:
        return arr[i]
    min_val = min(arr[i], get_min(arr, i + 1, n - 1))
    return min_val

def get_max(arr, i, n):
    if n == 1:
        return arr[i]
    max_val = max(arr[i], get_max(arr, i + 1, n - 1))
    return max_val

if __name__ == "__main__":
    main()
