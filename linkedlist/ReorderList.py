# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_LL(self,head):
        prev = None
        cur = head
        j = 0
        while cur:
            j+=1
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        node1 = head
        node2 = slow.next
        slow.next = None
        node2 = self.reverse_LL(node2)
        node = ListNode(0)
        cur = node
        while node1 or node2:
            if node1:
                cur.next = node1
                cur = cur.next
                node1 = node1.next
            if node2:
                cur.next = node2
                cur = cur.next
                node2 = node2.next
        node = node.next
