def search(arr, N, x):
    for i in range(0, N):
        if (arr[i] == x):
            return i
    return -1

def linear_search(arr, key, size):
    if size == 0:
        return -1
    elif arr[size - 1] == key:
        return size - 1
    else:
        return linear_search(arr, key, size - 1)


arr = [2, 3, 4, 10, 40]
x = 10
N = len(arr)

resault = search(arr, N, x)
if resault == -1:
    print("Element is not present in array")
else:
    print("Element in present as index", resault)

arr = [5, 15, 6, 9, 4]
key = 4
size = len(arr)
ans = linear_search(arr, key, size)
if ans != -1:
    print("The element", key, "is found at" , ans, "index of the given array.")
else:
    print("The element", key, "is not found.")
