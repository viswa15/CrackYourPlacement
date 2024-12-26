class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            columnNumber -= 1  # Adjust for 1-based indexing
            remainder = columnNumber % 26
            result = chr(remainder + ord('A')) + result
            columnNumber //= 26  # Move to the next significant digit
        return result
