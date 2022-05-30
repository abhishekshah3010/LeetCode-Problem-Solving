class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        array = [*s]
        left = 0
        right = len(s) - 1
        
        while left < right:
            if not array[left].isalpha():
                left+=1
                continue
            
            if not array[right].isalpha():
                right-=1
                continue
            
            array[left], array[right] = array[right], array[left]
            left, right = left + 1, right - 1
            
        return "".join(array)
            
            
        