# Given an integer array nums and an integer val, remove all occurrences of val 
# in nums in-place. The order of the elements may be changed. Then return the number 
# of elements in nums which are not equal to val.


def removeElement(nums, val):
    n = len(nums)
    if n == 0: return 0
    i = 0
    while i < n:
        if nums[i] == val:
            nums.pop(i)
            n-=1
        else:
            i+=1
    return n

nums1 = [3,2,2,3]
print(removeElement(nums1,2))
