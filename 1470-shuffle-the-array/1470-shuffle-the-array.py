class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # ans = []
        # for i in range(n):
        #     ans.append(nums[i])
        #     ans.append(nums[i+n])
        # return ans
        
        # ans = []
        # for i in range(n):
        #     ans.extend([nums[i], nums[i+n]])
        # return ans
    
        res = []
        for i, j in zip(nums[0:n],nums[n:]):
            res+=[i,j]
        return res                                                                                                      
        