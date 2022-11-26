def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - 1) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1

arr = [2, 3, 4, 10, 40]
x = 10

resault = binarySearch(arr, 0, len(arr)-1, x)

if resault != -1:
    print("Element in not present in array")
else:
    print("Element is not present in array")
