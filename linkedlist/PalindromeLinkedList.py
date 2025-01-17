# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_LL(self,head):
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        temp = head
        rhead = self.reverse_LL(slow)
        rtemp = rhead
        while rtemp:
            if rtemp.val != temp.val:
                return False
            rtemp = rtemp.next
            temp = temp.next
        return True

