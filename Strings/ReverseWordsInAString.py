class Solution:
    def reverseWords(self, s: str) -> str:
        r = s.split()
        return ' '.join(r[::-1])
