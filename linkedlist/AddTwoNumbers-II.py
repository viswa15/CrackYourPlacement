# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def to_number(head):
            c = 0
            while head:
                c = (c*10) + head.val
                head = head.next
            return c

        def to_LL(num):
            print(num)
            head = ListNode(0)
            cur = head
            for i in num:
                cur.next = ListNode(int(i))
                cur = cur.next
            return head.next


        num1 = to_number(l1)
        num2 = to_number(l2)

        res = to_LL(str(num1+num2))
        return res
