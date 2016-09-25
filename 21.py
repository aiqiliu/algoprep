# 21. Merge Two Sorted Lists
# Merge two sorted linked lists and return the head of the new linkd list

# 1. one of the list is mnull. return the other one
# two pointers pointing to l1, l2.
# create a new head with the smllest 
# while any of the pointer doesnt reach Null, keep comparing
# once ends. append the rest of the other list to the new lust 
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
        	return l2
        if l2 is None:
        	return l1
        dummy = ListNode(0)
        curr = dummy
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1 != None:
            curr.next = l1
        else:
            curr.next = l2
        return dummy.next



