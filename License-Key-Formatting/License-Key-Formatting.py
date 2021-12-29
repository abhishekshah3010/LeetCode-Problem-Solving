class Solution:
    """
    @param S: a string
    @param K: a integer
    @return: return a string
    """
    def licenseKeyFormatting(self, S, K):
        S = S.replace("-", "").upper()
        count = 0
        res = ""

        for c in S[::-1]:
            if count == K:
                res = "-" + res
                count = 0
            
            res = c + res
            count+=1
        return res
