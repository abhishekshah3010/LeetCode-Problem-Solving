class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        num_flips = 0
        num_ones = 0
        for num in s:
            if num =='1':
                num_ones += 1
            else:
                num_flips += 1
                if num_flips > num_ones:
                    num_flips = num_ones
                    
        return num_flips