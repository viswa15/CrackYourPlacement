class Solution:
    def index_checking(self,string):
        n = len(string)
        i = 0
        j = n-1
        m_i = 0
        m_j = 0
        while i<=j:
            if string[i] == string[j]:
                i+=1
                j-=1
                if i>j:
                    return True
            else:
                m_i = i
                m_j = j
                break

        i = m_i + 1
        j = m_j
        while i<=j:
            if string[i]==string[j]:
                i+=1
                j-=1
                if i>j:
                    return True
            else:
                break

        i=m_i
        j = m_j-1
        while i<=j:
            if string[i]==string[j]:
                i+=1
                j-=1
                if i>j:
                    return True
            else:
                break
        return False

    def validPalindrome(self, s: str) -> bool:
        res = self.index_checking(s)
        if res:
            return True
        else:
            return False