class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0 , len(s) -1 
        s = s.lower()
        
        while left < right:
            
            while s[left].isalnum() != True and left < right:
                left += 1 
            
            while s[right].isalnum() != True and left < right:
                right -= 1 
            
            if s[left].isalnum() and s[right].isalnum() and s[left] != s[right]:
                return False 
            
            left += 1 
            right -= 1 
        
        return True 
        