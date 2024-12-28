# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def to_arr(head):
            arr = []
            while head:
                arr.append(head.val)
                head = head.next
            return arr

        def to_LL(arr):
            head = ListNode(None)
            cur = head
            for i in arr:
                cur.next = ListNode(i)
                cur = cur.next
            return head.next

        arr = to_arr(head)
        l,r = left-1,right-1
        while l<=r:
            arr[l],arr[r] = arr[r],arr[l]
            l += 1
            r -= 1

        return to_LL(arr)