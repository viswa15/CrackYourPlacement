class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = float("inf")
        res=""
        for i in strs:
            l = min(l,len(i))
        for i in range(l):
            c = 0
            letter = strs[0][i]
            for word in strs:
                if word[i] == letter:
                    c+=1
            if c==len(strs):
                res += letter
            else:
                break
        return res