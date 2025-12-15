class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        s = "".join(ch for ch in s if ch.isalnum())

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
