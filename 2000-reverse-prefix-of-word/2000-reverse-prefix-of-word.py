class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i, c in enumerate(word):
            if c == ch:
                return word[:i+1][::-1] + word[i+1:]
        return word
        # index = word.find(ch)
        # return word[:index+1][::-1] + word[index+1:]
        