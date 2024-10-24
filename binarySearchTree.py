# Definition
# A Binary Search Tree is a binary tree where each node has a maximum of two children, referred to 
# as the left child and the right child. The key property of a BST is:

# For any given node, all keys in the left subtree are less than the node's key, and all keys in 
# the right subtree are greater than the node's key.

# Structure
# Node: Each node in a BST contains:
# A key (value).
# A reference to the left child (subtree).
# A reference to the right child (subtree).

# Basic Operations

# Search:
# Start at the root.
# If the target key equals the current node's key, the search is successful.
# If the target key is less, move to the left child; if greater, move to the right child.
# Repeat until found or a null reference is encountered.

# Insertion:
# Similar to searching; find the appropriate position based on the key comparison.
# Insert the new node as a leaf at the correct position.

# Deletion:
# Three cases:
# Node is a leaf: Simply remove the node.
# Node has one child: Remove the node and link its parent to its child.
# Node has two children: Replace the node with its in-order predecessor (maximum of the left subtree) or 
# in-order successor (minimum of the right subtree), then delete the predecessor or successor.

# Properties
# Time Complexity:

# Average case: O(log n) for search, insertion, and deletion.
# Worst case: O(n) (occurs when the tree becomes unbalanced, resembling a linked list).
# Space Complexity: O(n) for the storage of nodes.

# Height: The height of a balanced BST is log(n), while the height of an unbalanced BST can be n.

# Balancing BSTs
# To maintain efficiency, BSTs can become unbalanced. Balanced versions of BSTs include:

# AVL Trees: Self-balancing binary search trees where the difference in heights of left and right subtrees is at most one.
# Red-Black Trees: Another type of self-balancing BST that maintains a balance through color properties 
# (red or black) and rules regarding the parent-child relationship.

# Applications
# Searching: Fast retrieval of data.
# Sorting: In-order traversal of a BST produces a sorted sequence.
# Priority Queues: Can be implemented using BSTs.
# Databases: Often used for indexing and storing sorted data.

# Traversal Methods
# In-order: Left -> Node -> Right (yields sorted order).
# Pre-order: Node -> Left -> Right.
# Post-order: Left -> Right -> Node.
# Level-order: Visits nodes level by level (breadth-first).

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None

def inOrder(root):
    if not root: return
    inOrder(root.left)
    print(root.data, end = ", ")
    inOrder(root.right)

def  insertRecursively(root, data):
    newNode = Node(data)
    if not root:
        root = newNode
        return root
    if root.data < data:
        root.right = insertRecursively(root.right, data)
    else:
        root.left = insertRecursively(root.left, data)  
    return root

def searchRecursively(root, key):
    """Search for a key in the BST recursively."""
    if not root:  # Check if the node is None first
        return None  # Return None if the node does not exist
    if root.data == key:  # Check if the current node's data matches the key
        return root
    if key < root.data:  # If the key is less, search in the left subtree
        return searchRecursively(root.left, key)
    else:  # Otherwise, search in the right subtree
        return searchRecursively(root.right, key)


if __name__ == "__main__":
    # Creating the tree
    root = Node(10)

    print("\nRecursive inOrder DFS: ", end=' ')
    inOrder(root)
    print("\n-------------------------------------------")

    # Inserting nodes
    insertRecursively(root, 11)
    insertRecursively(root, 12)
    insertRecursively(root, 13)
    insertRecursively(root, 7)
    insertRecursively(root, 3)
    insertRecursively(root, 4)
    insertRecursively(root, 14)
    insertRecursively(root, 8)

    print("\nAfter inserting recursively: ", end=' ')
    inOrder(root)
    print("\n-------------------------------------------")

    # Searching for a key
    search_key = 13
    found_node = searchRecursively(root, search_key)
    if found_node:
        print(f"\nLooking for key {search_key} recursively - Found: {found_node.data}")
    else:
        print(f"\nLooking for key {search_key} recursively - Not Found")
    print("\n-------------------------------------------")
