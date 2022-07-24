class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(numbers):
            if n in d:
                return [d[n]+1, i+1]
            d[target-n] = i