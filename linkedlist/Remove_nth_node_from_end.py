# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        front = head
        back = head
        for i in range(n):
            front = front.next
        if front is None:
            return head.next
        while front.next:
            front = front.next
            back = back.next
        n = back.next
        back.next = back.next.next
        del n
        return head