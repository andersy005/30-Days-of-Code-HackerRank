"""You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8 """



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if (l1 is None and l2 is None):
            return None
            
        result = ListNode(0)
        current = result
        
        carry = 0
        
        while True:
            if l1 != None:
                carry += l1.val
                l1 = l1.next
                
                
            if l2 != None:
                carry += l2.val
                l2 = l2.next
                
            current.val = carry % 10
            carry = carry / 10
            
             # Create a new Node to hold the  next sum 
            if l1 != None or l2 != None or carry != 0:
                current.next = ListNode(0)
                current = current.next
                
            else:
                break
            
        return result