class Solution:
    def AddTwoNumbers(self, l1, l2):
        head = ListNode(0)
        cur = head
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10)
            carry = carry // 10
            cur = cur.next
        return head.next