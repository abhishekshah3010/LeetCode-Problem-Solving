class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        l, r = 0, len(s) - 1
        
        while l < r:
            c1, c2 = s[l], s[r]
            if c1.isalnum() and c2.isalnum():
                if c1 != c2:
                    return False
                l += 1
                r -= 1
            else:
                if not c1.isalnum():
                    l += 1
                if not c2.isalnum():
                    r -= 1
                    
        return True
        