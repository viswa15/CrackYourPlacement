class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        if needle==haystack:
            return 0
        if len(needle)==1:
            return haystack.index(needle[0])
        for i in range(len(haystack)):
            word=""
            for j in range(i,i+len(needle)):
                if j >= len(haystack):
                    break
                word+=haystack[j]
            print(word)
            if word==needle:
                return i