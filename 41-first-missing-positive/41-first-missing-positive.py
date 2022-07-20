class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        unique = set(nums)
        i = 1
        while i in unique:
            i+=1
        return i
        