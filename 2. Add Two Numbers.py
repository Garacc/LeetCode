# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1, num2 = 0, 0
        dig = 1
        while l1:
            num1 += l1.val * dig
            dig *= 10
            if l1.next == None: break
            l1 = l1.next
            
        dig = 1
        while l2:
            num2 += l2.val * dig
            dig *= 10
            if l2.next == None: break
            l2 = l2.next
        
        sumnum = num1 + num2
        
        if not sumnum: return ListNode(0)
        
        nodelist = []
        
        while sumnum:
            nodelist.append(ListNode(sumnum%10))
            sumnum = sumnum // 10
        for i in range(len(nodelist) - 1):
            nodelist[i].next = nodelist[i+1]
        
        return nodelist[0]