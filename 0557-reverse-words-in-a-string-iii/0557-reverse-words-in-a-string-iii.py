class Solution:
    def reverseWords(self, s: str) -> str:
        reversed_word = []
        words = s.split()
        for word in words:
            reverse_word = word[::-1]
            reversed_word.append(reverse_word)
        return " ".join(reversed_word)
    