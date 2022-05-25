class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        count = 0
        setnum = [int(s[i:i+k]) for i in range(len(s)-(k-1))]
        for n in setnum:
            if n != 0:
                if num % n == 0:
                    count += 1
        return count
                    
                    
        