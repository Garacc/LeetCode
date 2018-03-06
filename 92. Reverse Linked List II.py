class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n: return head
        
        dummy = ListNode(0)
        pre = dummy
        pre.next = head
        
        for i in range(m - 1):
            pre = pre.next
            
        reverse = None
        part = pre.next
        
        for _ in range(n - m + 1):
            cur = part
            part = part.next
            cur.next = reverse
            reverse = cur
        
        pre.next.next = part
        pre.next = reverse
        
        return dummy.next