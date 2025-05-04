def main():
    arr = []
    n = int(input("Enter the size of the array: "))
    print("Enter the elements of the array: ")
    for i in range(n):
        arr.append(int(input()))
    
    max_val = arr[0]
    for i in range(n):
        if max_val < arr[i]:
            max_val = arr[i]
    
    min_val = arr[0]
    for i in range(n):
        if min_val > arr[i]:
            min_val = arr[i]
    
    print("Largest element:", max_val)
    print("Smallest element:", min_val)

if __name__ == "__main__":
    main()
