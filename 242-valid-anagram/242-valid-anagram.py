class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = {}
        dic_t = {}
        
        for i in s:
            if i not in dic_s:
                dic_s[i] = 1
            else:
                dic_s[i] += 1
        
        for j in t:
            if j not in dic_t:
                dic_t[j] = 1
            else:
                dic_t[j] += 1
        
        if dic_s == dic_t:
            return True
        else:
            return False
            