class Solution:
    def multiply_two_lists(self, first, second):
        # Code here
        if not first or not second:
            return None

        num1,num2 = "",""
        while first:
            num1 += str(first.data)
            first = first.next
        while second:
            num2 += str(second.data)
            second = second.next


        return (int(num1) * int(num2))%1000000007