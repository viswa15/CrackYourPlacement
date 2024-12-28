# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        c = 0
        temp = head
        while temp:
            c+=1
            temp = temp.next
        if c%2==1:
            mid = c//2
            a = head
            for i in range(mid):
                a = a.next
            return a
        else:
            mid = c//2
            a = head
            for i in range(mid):
                a = a.next
            return a

