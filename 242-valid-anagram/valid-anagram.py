class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        cntArr = [0]*26
        for i in range(len(s)):
            tChar = ord(t[i]) -97
            sChar = ord(s[i]) -97
            cntArr[tChar] +=1
            cntArr[sChar] -=1

        for num in cntArr:
            if num != 0:
                return False
        return True