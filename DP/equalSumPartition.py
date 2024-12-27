def equalSumpartitionProblem(arr, x):
    n = len(arr)
    if n == 0 or x%2 != 0: return False
    else:
        return isSubsetSum(arr, x//2)
    
def isSubsetSum(arr, x):
    n = len(arr)
    # Initialize dp table with False values
    dp = [[False] * (x + 1) for _ in range(n + 1)]
    
    # Base case: If the sum is 0, it's always possible by choosing no elements
    for i in range(n + 1):
        dp[i][0] = True

    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(1, x + 1):
            if j < arr[i - 1]:
                dp[i][j] = dp[i - 1][j]  # Exclude the current element
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]  # Include or exclude the current element

    return dp[n][x]

def countNoOfSubsetsWithGivenSum(arr, target):
    n = len(arr)
    if n == 0 or target == 0: return 1
    dp = [[0]*(target+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(1, n+1):
        for j in range(1, target+1):
            if j >= arr[i-1]:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][target]




arr1 = [1,2,3003,4]
print(equalSumpartitionProblem(arr1, sum(arr1)))

arr2 = [1,5,5,11]
print(equalSumpartitionProblem(arr2, sum(arr2)))

arr3 = [2,3,5,6,8,10]
print(countNoOfSubsetsWithGivenSum(arr3, 10))
