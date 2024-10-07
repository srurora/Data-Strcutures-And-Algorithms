# Implement a Circular Singly Linked List
# traverse and print a Circular Singly Linked List
# insert node at the start of a Circular Singly Linked List
# insert node at the end of a Circular Singly Linked List
# remove first node from a Circular Singly Linked List

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self) -> None:
        self.head = None

    # insert node at the end of a Circular Singly Linked List
    def add_nodes_at_end(self, data):
        dummy = self.head
        curr = self.head
        new_node = Node(data)
        if dummy is None:
            new_node.next = new_node
            self.head = new_node
        else:
            while curr.next != dummy:
                curr = curr.next
            curr.next = new_node
            new_node.next = dummy

    # insert node at the start of a Circular Singly Linked List
    def add_nodes_at_start(self, data):
        new_node = Node(data)
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        print(curr.data)
        curr.next = new_node
        new_node.next = self.head
        self.head = new_node

    # remove first node from a Circular Singly Linked List
    def delete_first_node(self):
        curr = self.head
        second = self.head.next
        while curr.next != self.head:
            curr = curr.next
        curr.next = second
        self.head = second

    # traverse and print a Circular Singly Linked List
    def print_nodes(self):
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                print(self.head.data)
                break

if __name__ == "__main__":
    # Implement a Circular Singly Linked List
    cll = CircularLinkedList()
    cll.add_nodes_at_end(4)
    cll.add_nodes_at_end(3)
    cll.add_nodes_at_end(2)

    print("**********************************************")
    print("Add nodes at end")
    cll.print_nodes()

    print("**********************************************")
    print("Add nodes at start")
    cll.add_nodes_at_start(59)
    cll.print_nodes()

    print("**********************************************")
    print("delete the first node")
    cll.delete_first_node()
    cll.print_nodes()

