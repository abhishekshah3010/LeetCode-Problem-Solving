class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = sum(nums[:3])
        for i in range(len(nums)-2):
            k = len(nums)-1 
            j = i + 1 
          
            while j < k:
                close_sum = nums[i] + nums[j] + nums[k]
                
                if close_sum == target:
                    return close_sum
                
                if abs(close_sum - target) < abs(ans - target):
                    ans = close_sum
                
                if close_sum < target:
                    j += 1
                elif close_sum > target: 
                    k -= 1
                else: 
                    break
                          
        return ans