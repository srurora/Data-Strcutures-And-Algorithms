# Stacks
# Next Greater Element
# Valid Parentheses problem (Balanced Brackets)

# The functions associated with stack are:

# empty() – Returns whether the stack is empty – Time Complexity: O(1)
# size() – Returns the size of the stack – Time Complexity: O(1)
# top() / peek() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
# push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
# pop() – Deletes the topmost element of the stack – Time Complexity: O(1)

from collections import deque

stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)

print("Deleting elements using pop which pops out the last element of the stack:")
print(stack.pop())
print(stack.pop())

# Next Greater Element
def nextGreaterElementToRight(arr):
    result = [0]*len(arr)
    arr = arr[::-1]
    stack = []
    for i in range(len(arr)):
        if stack:
            while stack and stack[-1] <= arr[i]:
                stack.pop()
        if not stack:
            stack.append(arr[i])
            result[i] = -1
        else:
            result[i] = stack.pop()
        stack.append(arr[i])
    return result[::-1]
arr = [8, 4, 6, 9, 10, 1]
ans = nextGreaterElementToRight(arr)
print("Next greater element to te right:")
print(ans)

#Valid Parentheses problem (Balanced Brackets)
def checkValidParanthesis(arr):
    stack = []
    matching = {')':'(',
                 '}':'{', 
                 ']':'['
    }
    for i in arr:
        if i in matching.values():
            stack.append(i)
        elif i in matching:
            if not stack or stack.pop() != matching[i]:
                return False
        else:
            return False
    return not stack

s = '[]{}()'
print("Checking valid paranthesis:")
print(checkValidParanthesis(s))
s2 = '['
print("Checking valid paranthesis:")
print(checkValidParanthesis(s2))


