class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
            
        nums_sorted = sorted(nums)
        
        return(nums_sorted.index(num) for num in nums)
        
        