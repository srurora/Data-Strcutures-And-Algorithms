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
#  Remove loop from a Singly Linked List？
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
    
    def removeLoop(self, curr):
        startNode = self.head
        prev = Node(None)
        while startNode != curr:
            startNode = startNode.next
            prev = curr
            curr = curr.next
        prev.next = None
    
    # remove loop from a Singly Linked List
    def remove_loop_from_sll(self):
        curr = self.head
        fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            curr = curr.next
            if fast == curr:
                self.removeLoop(curr)

    #  Merge Two Sorted Lists Question
    def merge_two_sorted_LL(self, sll2):
        start1 = self.head
        start2 = sll2
        dummy = Node(0)
        prev = dummy
        while start1 and start2:
            if start1.data <= start2.data:
                prev.next = start1
                start1 = start1.next
            else:
                prev.next = start2
                start2 = start2.next
            prev = prev.next
        if start2 == None:
            prev.next = start1
        else:
            prev.next = start2
        return dummy.next
    
    #  LeetCode #2： Add Two Numbers
    def add_two_numbers(self, sll2):
        head1 = self.head
        head2 = sll2
        dummy = Node(0)
        prev = dummy
        carry = 0
        while head1 or head2:
            x = head1.data if head1 else 0
            y = head2.data if head2 else 0
            addition = carry + x + y
            carry = addition//10
            prev.next = Node(addition % 10)
            prev = prev.next
            if head1: head1 = head1.next
            if head2: head2 = head2.next
        if carry>0:
            prev.next = Node(carry)
        return dummy.next
               
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


    
if __name__ == "__main__":
    sll4 = SinglyLinkedList()
    sll4.add_node_at_last(1)
    sll4.add_node_at_last(1)
    sll4.add_node_at_last(9)

    sll5 = SinglyLinkedList()
    sll5.add_node_at_last(1)
    sll5.add_node_at_last(1)
    sll5.add_node_at_last(1)
    sll5.add_node_at_last(1)


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

    print("**********************************************")
    print("Remove the loop in the LL")
    sll3.remove_loop_from_sll()
    print("After Loop Removal")
    sll3.print_nodes()

    print("**********************************************")
    print("Merge two sorted singly LL")
    merged_list = SinglyLinkedList()
    merged_list.head = sll2.merge_two_sorted_LL(sll3.head)
    merged_list.print_nodes()

    print("**********************************************")
    print("Adding two numbers in singly LLs")
    merged_list = SinglyLinkedList()
    sll4.print_nodes()
    sll5.print_nodes()
    merged_list.head = sll4.add_two_numbers(sll5.head)
    merged_list.print_nodes()

    # ****************** End of Singly LLs **********************
    
    

    

    