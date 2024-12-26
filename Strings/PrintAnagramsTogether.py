class Solution:

    def Anagrams(self, words):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        #code here
        res = {}
        for s in words:
            count = [0]*26
            for i in s:
                count[ord(i)-ord("a")] += 1
            key = tuple(count)
            if key not in res:
                res[key] = []
            res[key].append(s)
        ans = []
        for i in res:
            ans.append(res[i])
        return ans
