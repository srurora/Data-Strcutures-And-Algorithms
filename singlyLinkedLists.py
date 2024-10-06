#  Create a Singly Linked List
#  Print elements of a Singly Linked List
#  Find length of a Singly Linked List
#  Insert nodes in a Singly Linked List
#  Delete nodes of a Singly Linked List
#  search an element in a Singly Linked List
#  Reverse a Singly Linked List
#  find nth node from the end of a Singly Linked List
#  remove duplicate from sorted Singly Linked List
#  insert a node in a sorted Singly Linked List
#  remove a given key from Singly Linked List
#  detect a loop in a Singly Linked List
#  find start of a loop in a Singly Linked List？
#  Why Floyd's Cycle Detection algorithm works？
#  remove loop from a Singly Linked List？
#  Merge Two Sorted Lists Question
#  LeetCode #2： Add Two Numbers

class SinglyLinkedList:
    def __init__(self):
        self.head = None

#  Insert nodes in a Singly Linked List
    def add_node_at_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

#  Insert nodes in a Singly Linked List
    def add_node_at_start(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

#  Insert nodes in a Singly Linked List
    def add_node_after_a_given_data_point(self, data1, data2):
        new_node = Node(data2)
        if self.head == None:
            new_node = self.head
        curr = self.head
        while curr.next:
            if curr.data == data1:
                new_node.next = curr.next  
                curr.next = new_node 
            curr = curr.next

    #Delete nodes of a Singly Linked List        
    def delete_node(self, data):
        if self.head == None: return "No node to delete"
        else:
            prev = self.head
            curr = self.head.next
            while curr:
                if curr.data == data:
                    prev.next = curr.next
                    return
                prev = prev.next
                curr = curr.next

    #Delete last node of a Singly Linked List        
    def delete_last_node(self):
        if self.head == None: return "No node to delete"
        else:
           curr = self.head.next
           prev = self.head
           while curr.next is not None:
               curr =  curr.next
               prev = prev.next
           prev.next = None

    #Delete first node of a Singly Linked List        
    def delete_first_node(self):
        if self.head == None: return "No node to delete"
        else:
          self.head = self.head.next

   #Delete node of a Singly Linked List when position is given       
    def delete_node_with_position(self, position):
        if self.head == None: return "No node to delete"
        else:
         curr = self.head.next
         prev = self.head
         curr_position = 1
         while curr.next:
             if curr_position == position:
                 prev.next = curr.next
                 return
             curr = curr.next
             prev = prev.next
             curr_position+=1
           

  #  search an element in a Singly Linked List
    def search_node(self, data):
        if self.head is None: return "NO valid LL"
        else:
            curr = self.head
            i = 1
            while curr:
                if curr.data == data:
                    print("Node found at:", i, "th node")
                    return
                curr = curr.next
                i+=1
        return ("Not found")
        

    #  Reverse a Singly Linked List
    def reverse_ll(self):
        if self.head is None: return "No valid LL"
        else:
            curr = self.head
            prev = None
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            self.head = prev
                   
    #  Print elements of a Singly Linked List            
    def print_nodes(self):
        curr = self.head
        while curr:
            print(curr.data, end="-->")
            curr = curr.next
        print("null")

   # Find length of a Singly Linked List
    def length_of_sll(self):
        length = 0
        if self.head is None: return 0
        else:
            curr = self.head
            while curr:
                length+=1
                curr = curr.next
        return length
    
    #  find nth node from the end of a Singly Linked List
    def find_nth_node(self, n):
        if self.head == None: return
        else:
            n-=1
            curr = self.head
            while curr.next and n!=0:
                curr = curr.next
                n-=1
        print(curr.data)

    #  remove duplicate from sorted Singly Linked List
    def remove_dups(self):
        curr = self.head
        while curr and curr.next:
            if curr.data == curr.next.data:
               curr.next = curr.next.next
            else:
                curr = curr.next
    
    #  insert a node in a sorted Singly Linked List
    def insertInSortedSLL(self, nodeData):
        newNode = Node(nodeData)
        curr = self.head.next
        prev = self.head
        #if node needs to be added in the start
        if prev and prev.data > nodeData:
            newNode.next = prev
            return
        else:
            while curr:
                #if node needs to be added in the middle
                if curr.data > nodeData:
                    prev.next = newNode
                    newNode.next = curr
                    return
                #if node needs to be added in the end
                elif curr.data < nodeData and curr.next == None:
                    curr.next = newNode
                    newNode.next = None
                    return
                prev = prev.next
                curr = curr.next

    #  insert a node in a sorted Singly Linked List(Simpler Approach)
    def insert_node_in_sorted_sll_simple(self, nodeData):
        newNode = Node(nodeData)
        curr = self.head
        prev = Node(None)
        #Adding node at the start
        if curr and curr.data > nodeData:
            newNode.next = curr
            self.head = newNode
            return
        while curr and curr.data < nodeData:
            prev = curr
            curr = curr.next
        newNode.next = curr
        prev.next = newNode

    #  remove a given key from Singly Linked List
    def remove_given_key(self, key):
        curr = self.head
        prev = Node(None)
        if curr and curr.data == key:
            prev = curr.next
            curr.next = None
            self.head = prev
            return
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        prev.next = curr.next

    #To check the working of the detect the loop function below
    def create_loop(self, position):
        """Creates a loop in the list. The loop starts at the given position (0-indexed)."""
        if position < 0:
            return
        loop_start_node = None
        current = self.head
        index = 0
        while current:
            if index == position:
                loop_start_node = current
            current = current.next
            index += 1
        if loop_start_node:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = loop_start_node  # Creating the loop

    #detect a loop in a Singly Linked List
    def detect_a_loop_in_a_SLL(self):
        curr = self.head
        fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            curr = curr.next
            if fast == curr:
                print("Loop detected")
                return
        print("No Loop Detected")

    #Helper function for find_start_of_a_loop
    def findTheStart(self, slow):
        temp = self.head
        while slow != temp:
            temp = temp.next
            slow = slow.next
        return temp.data

    #  find start of a loop in a Singly Linked List？
    def find_start_of_a_loop(self):
        curr = self.head
        fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            curr = curr.next
            if curr == fast:
            # Find the starting node of the loop
                data = self.findTheStart(curr)
                print("Loop starts at:", data)
                return data
        print("No loop detected")
        return None
    
    # remove loop from a Singly Linked List



               
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


    
if __name__ == "__main__":
    sll3 = SinglyLinkedList()
    sll3.add_node_at_last(0)
    sll3.add_node_at_last(1)
    sll3.add_node_at_last(2)
    sll3.add_node_at_last(3)
    # Create a loop for testing
    sll3.create_loop(3)

    # Create a LinkedList object
    sll = SinglyLinkedList()

    sll2 = SinglyLinkedList()

    sll2.add_node_at_last(10)
    sll2.add_node_at_last(10)
    sll2.add_node_at_last(20)
    sll2.add_node_at_last(20)
    sll2.add_node_at_last(30)
    sll2.add_node_at_last(30)
    
    #adding elements to the SLL
    sll.add_node_at_last(10)
    sll.add_node_at_last(20)
    sll.add_node_at_last(30)
    sll.add_node_at_last(40)
    sll.add_node_at_last(50)

    sll.add_node_at_start(60)
    # printing all nodes in SLL
    print("**********************************************")
    
    print("SINGLY LL is as follows:")
    sll.print_nodes()
    print("**********************************************")
    
    #printing the length of the SLL
    print("Length of the sll:")
    print(sll.length_of_sll())
    print("**********************************************")
    
    sll.add_node_after_a_given_data_point(30, 70)
    print("SINGLY LL after adding a node after data = 30")
    sll.print_nodes()
    
    print("**********************************************")
    sll.delete_node(70)
    print("SINGLY LL after deleting a node data = 70")
    sll.print_nodes()

    print("**********************************************")
    sll.delete_last_node()
    print("SINGLY LL after deleting last node")
    sll.print_nodes()

    print("**********************************************")
    sll.delete_first_node()
    print("SINGLY LL after deleting first node which is 60")
    sll.print_nodes()

    print("**********************************************")
    sll.delete_node_with_position(2)
    print("SINGLY LL after deleting node at position 2")
    sll.print_nodes()

    print("**********************************************")
    print("searching for a node with data = 40")
    sll.search_node(40)

    print("**********************************************")
    print("Reverse the LL")
    sll.reverse_ll()
    sll.print_nodes()

    print("**********************************************")
    print("Finding the nth node, here n = 2")
    sll.find_nth_node(2)

    print("**********************************************")
    print("Removing duplicates in a sorted LL")
    sll2.remove_dups()
    sll2.print_nodes()

    print("**********************************************")
    print("Adding a new node in a sorted LL")
    sll2.insertInSortedSLL(12)
    sll2.insertInSortedSLL(40)
    sll2.insert_node_in_sorted_sll_simple(32)
    sll2.insert_node_in_sorted_sll_simple(1)
    sll2.insert_node_in_sorted_sll_simple(44)
    sll2.print_nodes()

    print("**********************************************")
    print("remove a given key from Singly Linked List")
    sll2.remove_given_key(1)
    sll2.remove_given_key(44)
    sll2.print_nodes()

    print("**********************************************")
    print("Detecting a Loop in Singly Linked List")
    sll2.detect_a_loop_in_a_SLL()
    sll2.print_nodes()
    sll3.detect_a_loop_in_a_SLL()

    print("**********************************************")
    print("Finding start of the loop")
    sll3.find_start_of_a_loop()

    