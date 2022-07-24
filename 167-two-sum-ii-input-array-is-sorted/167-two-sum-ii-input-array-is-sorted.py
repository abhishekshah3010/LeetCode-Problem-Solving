class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # d = {}
        # for i, n in enumerate(numbers):
        #     if n in d:
        #         return [d[n]+1, i+1]
        #     d[target-n] = i
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1
