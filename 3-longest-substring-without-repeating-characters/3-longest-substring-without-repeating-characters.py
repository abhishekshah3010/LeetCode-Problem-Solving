class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = set()
        left = 0
        right = 0
        
        # if len(s) == 0:
        #     return 0
        
        res = float("-inf")
        
        while right < len(s):
            if s[right] in curr:
                curr.remove(s[left])
                left += 1
            elif s[right] not in curr:
                curr.add(s[right])
                res = max(res, right - left + 1)
                right += 1
        
        return res if len(s) != 0 else 0
        