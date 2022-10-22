class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums = sorted(nums)
        
        for i in range(len(nums)):
            l = i+1
            r = len(nums) - 1
            tar = 0 - nums[i]
            while l<r:
                if nums[l] + nums[r] == tar:
                    res.add((nums[i], nums[l], nums[r]))
                    l+=1
                    r-=1
                elif nums[l] + nums[r] < tar:
                    l+=1
                else:
                    r-=1
        return [list(r) for r in res]
        
        
        
        