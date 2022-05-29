class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words = [i[::-1] for i in words]
        ans = " ".join(words)
        return ans
        