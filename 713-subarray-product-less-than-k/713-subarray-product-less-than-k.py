class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        left = 0
        product = 1
        count = 0
        
        for num in range(len(nums)):
            product *= nums[num]
            
            while left < len(nums) and product >= k:
                product/=nums[left]
                left+=1
                
            if k > product:
                count = count + (num - left + 1)
            
        return count
        