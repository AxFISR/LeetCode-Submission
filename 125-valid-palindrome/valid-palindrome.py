class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        skipIndex = 0
        newstr = ""
        #gonna rewrite the enire string, keeping only the letters

        for skipIndex in range(len(s)):
            if ord(s[skipIndex]) >= 65 and ord(s[skipIndex]) <= 90:
                newstr += chr(ord(s[skipIndex]) + 32)
            elif ord(s[skipIndex]) >= 97 and ord(s[skipIndex]) <= 122:
                newstr += s[skipIndex]
            elif ord(s[skipIndex]) >= 48 and ord(s[skipIndex]) <= 57:
                newstr += s[skipIndex]
            else:
                continue

        l=0
        r=len(newstr)-1
        while(l<r):
            if(newstr[l] != newstr[r]):
                return False
            l+=1
            r-=1
        return True