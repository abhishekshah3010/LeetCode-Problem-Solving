class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0] * len(nums)
        right = [0] * len(nums)
        
        left[0] = 1
        right[-1] = 1
        res = []
        
        for i in range(1, len(nums)):
            left[i] = left[i-1]*nums[i-1]
            right[len(nums)-i-1] = right[len(nums)-i]*nums[len(nums)-i]
            
        for j in range(len(nums)):
            res.append(left[j]*right[j])
        
        return res
        