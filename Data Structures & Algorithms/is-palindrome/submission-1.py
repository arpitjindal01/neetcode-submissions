class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for ch in s:
            if ch.isalnum():
                cleaned+=ch.lower()
        print(cleaned)
        return cleaned == cleaned[::-1]