#Print elements of the array
#Remove Even Integers from an Array
#Reverse an Array
#find Minimum value in an Array
#Find Second Maximum value in an Array
#move Zeroes to end of an Array
#Find the Missing Number in an Array
#check if a given String is a Palindrome

# Function to print elements of an array
def print_array(arr):
    print("Elements of the array are:")
    for element in arr:
        print(element)

# Function to Remove Even Integers from an Array
def remove_even_integers(arr):
    print("Removing Even Integers:")
    for i in arr:
        if i%2 == 0:
            del i
    for element in arr:
        print(element)

def reverse_an_array_1(arr):
    print("Direct method of Reversing arr")
    arr = arr[::-1]
    for element in arr:
        print(element)

def reverse_an_array_2(arr):
    print("Algorithmic method of Reversing arr:")
    start = 0
    end = len(arr)-1
    while start<end:
        arr[start], arr[end] = arr[end], arr[start]
        start+=1
        end-=1
    for element in arr:
        print(element)

def find_min_value(arr):
    #Minimum value in an Array
    print("Minimum value in an Array:")
    minimum = float('inf')
    for i in range(len(arr)):
        if arr[i] < minimum:
            minimum = arr[i]
    print(minimum)

def find_second_max(arr):
    print("Second Max value in an Array:")
    maximum = float('-inf')
    second_maximum = float('-inf')
    for i in range(len(arr)):
        if arr[i] > maximum:
            second_maximum = maximum
            maximum = arr[i]
        elif arr[i] != maximum and arr[i] > second_maximum:
            second_maximum = arr[i]
    print(second_maximum)

def move_zeros_to_end(arr):
    #move Zeroes to end of an Array
    #2-pointers method
    print("After moving zeroes to the end:")
    #j will focus on zero elements
    j = 0
    #i will focus on non-zero element
    for i in range(len(arr)):
        if arr[i] != 0 and arr[j] == 0 and j<len(arr):
            arr[i], arr[j] = arr[j], arr[i]
        if arr[j]!=0:
            j+=1
    for i in arr:
        print(i)

#Find the Missing Number in an Array
def find_missing_number(arr):
    print("Missing Number in the Array is:")
    n = len(arr) + 1
    #using mathematical formula
    total_sum_exp = (n*(n+1))//2
    total_sum_actual = 0
    for i in range(n-1):
        total_sum_actual+=arr[i]
    print(total_sum_exp - total_sum_actual)

def check_if_string_is_palindrome(palindrome):
    print("Checking is string is palindrome:")
    left = 0
    right = len(palindrome)-1
    while left <= right:
        if(palindrome[left] != palindrome[right]):
            return False
        left+=1
        right -=1
    return True

# Main function
def main():
    # Define array
    arr = [10, 20, 30, 40, 50]
    arr2 = [0, 20, 0, 40, 0]
    arr3 =[1,2,4,5,6,7,8,9]
    palindrome1 = "madam"
    palindrome2 = "sir"

    # Call the function to print the array
    print_array(arr)
    remove_even_integers(arr)
    reverse_an_array_1(arr)
    reverse_an_array_2(arr)
    find_min_value(arr)
    find_second_max(arr)
    move_zeros_to_end(arr2)
    find_missing_number(arr3)
    print("True") if check_if_string_is_palindrome(palindrome1) else print("False")
    print("True") if check_if_string_is_palindrome(palindrome2) else print("False")

# Entry point of the program
if __name__ == "__main__":
    main()
