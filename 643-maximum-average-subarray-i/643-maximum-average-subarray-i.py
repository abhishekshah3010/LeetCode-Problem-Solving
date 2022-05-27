class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = maxSum = sum(nums[:k])
        
        for i in range(k, len(nums)):
            window += nums[i] - nums[i-k]
            maxSum = max(maxSum, window)
            
        return maxSum/k
