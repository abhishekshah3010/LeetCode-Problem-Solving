class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                dic[n] += 1
        dic = dict(sorted(dic.items(), key = lambda i: i[1], reverse=True))
        print(dic)
        return list(dic.keys())[:k]
        
        