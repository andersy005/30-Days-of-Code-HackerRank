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

