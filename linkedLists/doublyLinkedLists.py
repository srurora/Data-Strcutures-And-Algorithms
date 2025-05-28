# represent a Doubly Linked List
# implement Doubly Linked List
# print elements of a Doubly Linked List
# insert node at the beginning of a Doubly Linked List
# Insert node at the end of a Doubly Linked List
# delete first node in a Doubly Linked List
# delete last node in a Doubly Linked List

# represent a Doubly Linked List
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

# represent a Doubly Linked List
class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None

   # Insert node at the end of a Doubly Linked List
    def add_nodes_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr

   # insert node at the beginning of a Doubly Linked List
    def add_nodes_at_start(self, data):
        new_node = Node(data)
        if self.head is None: self.head = new_node
        else:
            first = self.head
            first.prev = new_node
            new_node.next = first
            self.head = new_node

    # delete first node in a Doubly Linked List
    def delete_first_Node(self):
        curr = self.head
        new_head = curr.next
        curr.next = None
        new_head.prev = None
        self.head = new_head

    # delete last node in a Doubly Linked List
    def delete_last_node(self):
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.prev = None

    # delete last node in a Doubly Linked List
    def delete_the_last_node(self):
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.prev.next = None
        curr.prev = None
         
    def print_nodes(self):
        start = self.head
        while start:
            print(start.data, end="-->")
            start = start.next
        print("null")

if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.add_nodes_at_end(1)
    dll.add_nodes_at_end(2)
    print("**********************************************")
    print("Add nodes at end")
    dll.print_nodes()

    dll.add_nodes_at_start(3)
    print("**********************************************")
    print("Add nodes at start")
    dll.print_nodes()

    print("**********************************************")
    print("Delete first Node")
    dll.delete_first_Node()
    dll.print_nodes()

    print("**********************************************")
    print("Delete last Node")
    dll.delete_the_last_node()
    dll.print_nodes()



        