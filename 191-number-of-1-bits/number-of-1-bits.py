class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        mask = 1
        while(n > 0):
            if(n&1 > 0):
                cnt+=1
            n = n>>1
        return cnt