# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        numlist = []
        while head:
            numlist.append(head.val)
            if head.next == None: break
            head = head.next
        return numlist == numlist[::-1]