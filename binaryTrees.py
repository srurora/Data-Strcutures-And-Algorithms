# Tree represents the nodes connected by edges. It is a non-linear data structure. It has the following properties −
# One node is marked as Root node.
# Every node other than the root is associated with one parent node.
# Each node can have an arbiatry number of chid node.

# What is Binary Tree?
# Binary tree is a tree data structure(non-linear) in which each node can have at most two children which are referred to as the left child and the right child. 
# The topmost node in a binary tree is called the root, and the bottom-most nodes are called leaves. A binary tree can be visualized as a hierarchical structure with the root at the top and the leaves at the bottom.

# Each node in a Binary Tree has three parts:
# Data
# Pointer to the left child
# Pointer to the right child

# Terminologies in Binary Tree
# Nodes: The fundamental part of a binary tree, where each node contains data and link to two child nodes.
# Root: The topmost node in a tree is known as the root node. It has no parent and serves as the starting point for all nodes in the tree.
# Parent Node: A node that has one or more child nodes. In a binary tree, each node can have at most two children.
# Child Node: A node that is a descendant of another node (its parent).
# Leaf Node: A node that does not have any children or both children are null.
# Internal Node: A node that has at least one child. This includes all nodes except the root and the leaf nodes.
# Depth of a Node: The number of edges from a specific node to the root node. The depth of the root node is zero.
# Height of a Binary Tree: The number of nodes from the deepest leaf node to the root node.

# Properties of Binary Tree
# The maximum number of nodes at level L of a binary tree is 2L
# The maximum number of nodes in a binary tree of height H is 2H – 1
# Total number of leaf nodes in a binary tree = total number of nodes with 2 children + 1
# In a Binary Tree with N nodes, the minimum possible height or the minimum number of levels is Log2(N+1)
# A Binary Tree with L leaves has at least | Log2L |+ 1 levels

# Traversal in Binary Tree:
# Two Types: DFS(Recursion) and BFS(Queue)
# DFS ---> 3 types ----> PreOrder, Inorder, PostOrder
# Preorder = Node --> Left ----> Right
# Inorder = Left ---> Node ----> Right
# Postorder = Left ---> Right ---> Node
# BFS : Explores all nodes at the current depth before moving to the next depth

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None

# Recursive  preorder 
def preOrder(node):
        if node is None: 
              return
        print(node.data, end=",")
        preOrder(node.left)
        preOrder(node.right)

# Recursive inorder
def inOrder(node):
        if node is None: 
              return
        inOrder(node.left)
        print(node.data, end=',')
        inOrder(node.right)

# Recursive postorder
def postOrder(node):
        if node is None: 
              return
        postOrder(node.left)
        postOrder(node.right)
        print(node.data, end=",")

#Iterative preOrder using stack
def iterativePreOrder(node):
      if node is None: return
      stack = []
      stack.append(node)
      while(len(stack) > 0):
        # Pop the top item from stack and print it
        node = stack.pop()
        print (node.data, end=",") 

        # Push right and left children of the popped node
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)

#Iterative Inorder using stack
def iterativeInOrder(node):
    if not node: return
    stack = []
    while stack or node:
        # Traverse to the leftmost node
        while node:
            stack.append(node)
            node = node.left    
        # Process the node
        node = stack.pop()
        print(node.data, end=",")       
        # Move to the right node
        node = node.right

#Iterative post-order using stack: left--right--node
def iterativePostOrder(node):
    if not node: return
    stack = [node]
    visited = [False]
    result = []
    while stack:
        curr, v = stack.pop(), visited.pop()
        if v:
             result.append(curr.data)
        else:
             stack.append(curr)
             visited.append(True)
             if curr.right:
                stack.append(curr.right)
                visited.append(False)
             if curr.left:
                stack.append(curr.left)
                visited.append(False)
    print(result)

def iterativeFindMax(root):
     if not root: return
     stack = [root]
     maxU = float('-inf')
     while stack:
          curr = stack.pop()
          maxU = max(maxU, curr.data)
          if curr.right:
               stack.append(curr.right)
          if curr.left:
               stack.append(curr.left)
     print(maxU)

def findMax(root):
     if not root: return
     maxU = root.data
     left = float('-inf')
     right = float('-inf')
     if root.left:
        left = findMax(root.left)
     if root.right:
        right = findMax(root.right)
     return max(maxU, left, right)
             
if __name__ == "__main__":
    # Creating the tree
    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)

    print("\nRecursive Pre-order DFS: ", end=' ')
    preOrder(root)
    print("\nIterative Pre-order DFS: ", end=' ')
    iterativePreOrder(root)
    print("\n-------------------------------------------")

    print("\nRecursive in-order DFS: ", end=' ')
    inOrder(root)
    print("\nIterative in-order DFS: ", end=' ')
    iterativeInOrder(root)
    print("\n-------------------------------------------")


    print("\nRecursive Post-order DFS: ", end=' ')
    postOrder(root)
    print("\nIterative Post-order DFS: ", end=' ')
    iterativePostOrder(root)
    print("\n-------------------------------------------")

    print("\nRecursive - Find Max in BT: ", end=' ')
    print(findMax(root))
    print("\nIterative - Find Max in BT: ", end=' ')
    iterativeFindMax(root)
    print("\n-------------------------------------------")

    
       
