# Node class:

class Node:

    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as Null


# Linked List class
class LinkedList:

    # Function to initialize the Linked List object
    def __init__(self):
        self.head = None 

    # Function prints contents of linked list
    def printList(self):
        temp = self.head
        while(temp):
            print temp.data
            temp = temp.next

    # Function that insert a new node at the beginning
    def insertatBeginning(self, new_data):

        new_node = Node(new_data)
        new_node.next = self.head   # Make next of new node as head
        self.head = new_node        # Make the head to point to new Node 


    # Function that  inserts a new node after the given prev_node
    def insertAfterGivenNode(self, prev_node, new_data):

        # Check if the given prev_node exists
        if prev_node is None:
            print "The given previous node must be in LinkedList"
            return 

        new_node = Node(new_data)
        new_node.next = prev_node.next  # Make next of new Node as next of prev_node
        prev_node.next = new_node       # Make next of prev_node as new_node


if __name__ == "__main__":

    # Start with the empty list
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third
    print"#" * 50
    llist.printList()

    print"#" * 50
    llist.insertatBeginning(0)
    llist.printList()

    print"#" * 50
    llist.insertAfterGivenNode(llist.head.next.next, 20)
    llist.printList()