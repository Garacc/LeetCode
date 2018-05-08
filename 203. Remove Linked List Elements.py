# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head: return None
        
        while head.val == val:
            head = head.next
            if head == None: return head
        
        node = head
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
                continue
            else:
                node = node.next
        
        return head
        
                