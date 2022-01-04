class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                
        # d={}
        # for i,num in enumerate(nums):
        #     if num in d:
        #         return [d[num],i]
        #     else:
        #         d[target-num]=i
    
        