def linear_search(arr, target):
    if not arr: return -1
    n = len(arr)
    for i in range(n):
        if arr[i] == target: return i
    return -1

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            low = mid + 1 
        else:
            high = mid - 1  

    return -1 

def binary_search_recursive(arr, target):
    low, high = 0, len(arr)-1
    if low > high: return -1
    mid = (low + high)//2
    if arr[mid] == target: return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr[mid+1:], target)
    else: 
        return binary_search_recursive(arr[:mid-1], target)

arr1 = [2,3,4,1,0,5]
print("result of linear search:", linear_search(arr1, 5))

arr2 = [5, 7, 8, 9, 11, 16, 18]
print("result of binary search:", binary_search(arr2, 5))

print("result of binary search:", binary_search(arr2, 99))

print("result of binary search recursive:", binary_search_recursive(arr2, 99))

print("result of binary search recursive:", binary_search_recursive(arr2, 5))