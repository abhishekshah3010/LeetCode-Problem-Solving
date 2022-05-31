class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        t = 0
        c = None
        for r in range(len(nums)):
            t+=nums[r]
            
            while t >= target:
                c = min(c or float('inf'), r+1-l)
                t-=nums[l]
                l+=1
        return c or 0 
        
        # if len(nums) == 0: 
        #     return 0
        # i, j = 0, 0
        # c, t = float("inf"), nums[0]
        # while j < len(nums):
        #     if t < target:
        #         j += 1
        #         if j < len(nums):
        #             t += nums[j]
        #     elif t >= target:
        #         c = min(j - i + 1, c)
        #         t -= nums[i]
        #         i += 1
        # return c if c != float("inf") else 0
                
        
                
            
        