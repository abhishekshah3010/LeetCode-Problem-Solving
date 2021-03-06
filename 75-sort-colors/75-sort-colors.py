class Solution:
    def sortColors(self, nums: List[int]) -> None:
        c0 = c1 = c2 = 0
        for num in nums:
            if num == 0:
                c0 += 1
            elif num == 1:
                c1+=1
            else:
                c2+=1
        
        nums[:c0] = [0] * c0
        nums[c0:c1+c0] = [1] * c1
        nums[c1+c0:] = [2] * c2
        
        