#Given an integer array nums, return the length of the longest strictly increasing subsequence

def lengthOfLIS(arr):
    n = len(arr)
    if n == 0: return 0
    dp = [1]*n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[j]+1, dp[i])
    return max(dp)

arr1 = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(arr1))


def removeDuplicates(nums) -> int:
        n = len(nums)
        if n == 0: return 0
        counts = {}
        i = 0
        while i < n:
            if nums[i] in counts:
                nums.pop(i)
                n-=1
            else:
                counts[nums[i]]=1
                i+=1
        return n
arr2 = [10,9,9,9]
print(removeDuplicates(arr2))

# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element
#  appears at most twice. The relative order of the elements should be kept the same.
def removeDuplicatesII(nums) -> int:
        n, i = len(nums), 0
        counts = {}
        while i < n:
            if nums[i] in counts and counts[nums[i]] >= 2:
                nums.pop(i)
                n-=1
            elif nums[i] in counts and counts[nums[i]] < 2:
                counts[nums[i]]+=1
                i+=1
            else:
                counts[nums[i]] = 1
                i+=1
        print(counts)
        return n
        