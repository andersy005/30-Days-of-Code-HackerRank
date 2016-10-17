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


if __name__ == "__main__":

    # Start with the empty list
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third

    llist.printList()