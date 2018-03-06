# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    '''
    TLE
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        
        if head is None or head.next is None: return
        
        cp = head
        np = cp.next
        while np:
            np = self.reverseList(np)
            cp.next = np
            cp = np
            np = np.next
        
    
    copy from 206
        
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        while head:
            cur = head
            head = head.next
            cur.next = pre
            pre = cur
        return pre
    '''
    def reorderList(self, head):
        if not head:
            return
            
        # find the mid point
        slow = fast = head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    
        # reverse the second half in-place
        pre, node = None, slow
        while node:
            pre, node.next, node = node, pre, node.next
        
        # Merge in-place; Note : the last node of "first" and "second" are the same
        first, second = head, pre
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
        return 