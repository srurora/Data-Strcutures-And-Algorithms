def BubbleSort(arr):
    x = len(arr)
    for n in range(x-1, 0 , -1):
        swapped = False
        for i in range(n):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        if not swapped:
            break
    return arr

# Outer loop: Iterates through each element of the array.
# Finding the minimum: Finds the index of the minimum element in the unsorted portion of the array. 
# Swapping: Swaps the current element with the minimum element found.
# Repeat: Continues until the entire array is sorted.
def SelectionSort(arr):
    n = len(arr)
    for i in range(n):
        minimum = i
        for j in range(i+1, n):
            if arr[j]<arr[minimum]:
                minimum = j
        arr[i], arr[minimum] = arr[minimum], arr[i]
    return arr

# Outer loop: Iterates through the array starting from the 
#             second element (index 1) because the first element is considered already sorted.
# Inner loop: Compares the current element (key) with the elements
#             in the sorted part of the array (on the left) and shifts larger elements one position to the right.
# Insertion:  Inserts the key at the correct position in the sorted part of the array.
def InsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr

def merge(left, right):
    final = []
    i, j = 0, 0
    while i < len(left) and j< len(right):
        if left[i] < right[j]:
            final.append(left[i])
            i+=1
        else:
            final.append(right[j])
            j+=1
    final.extend(left[i:])
    final.extend(right[j:])
    return final


def MergeSort(arr):
    n = len(arr)
    if n <= 1: return arr
    mid = n // 2
    left, right = arr[:mid], arr[mid:]
    sorted_left = MergeSort(left)
    sorted_right = MergeSort(right)
    return merge(sorted_left, sorted_right)

def QuickSort(arr):
    n = len(arr)
    if n <= 1: return arr
    pivot = arr[-1]
    left, right = [], []
    for num in arr[:-1]:
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)
    return QuickSort(left) + [pivot] + QuickSort(right)

def CountingSort(arr):
    if not arr:
        return []  # Handle empty array edge case

    # Step 1: Find the range of the array
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    # Step 2: Create a count array to store the frequency of each element
    count = [0] * range_of_elements

    for num in arr:
        count[num - min_val] += 1  # Adjust index for negative numbers

    # Step 3: Modify the count array to store cumulative counts
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Step 4: Build the output array
    output = [0] * len(arr)
    for num in reversed(arr):  # Traverse in reverse to maintain stability
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output
    

arr = [9,4,6,5,2,1,8]
print("Result of Bubble Sort:", BubbleSort(arr))
print("Result of Selection Sort:", SelectionSort(arr))
print("Result of Insertion Sort:", InsertionSort(arr))
print("Result of Merge Sort:", MergeSort(arr))
print("Result of Quick Sort:", QuickSort(arr))
print("Result of Counting Sort:", CountingSort(arr))