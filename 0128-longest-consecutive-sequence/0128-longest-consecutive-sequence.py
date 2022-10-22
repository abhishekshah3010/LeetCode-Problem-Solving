class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s, longest = set(nums), 0
        
        for num in s:
            if num - 1 not in s:
                j = 0
                while num + j in s:
                    j+=1
                longest = max(longest, j)
        return longest
        
        