# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = new ListNode()
        dummy.val = 0
        dummy.next = head
        first, second = dummy, dummy
        i = 0
        while i < n + 1:
            first = first.next
        while first not None:
            second = second.next
            first = first.next
        second = second.next.next
        return dummy.next

  if head is None:
            return head
        
        if head.next is None:
            head = head.next
            return head
            
        list_len = 0
        curr = head
        while curr != None:
            list_len += 1
            curr = curr.next
       
        if n == list_len:
            head = head.next
            return head
        target = list_len - n
        i = 1
        prev = head
        curr = prev.next
        next = curr.next
        while i < target:
            prev = curr
            curr = curr.next
            next = next.next
            i += 1
        prev.next = next
        return head
            
            
                                                                                                                              