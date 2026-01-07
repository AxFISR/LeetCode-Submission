class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        newNum = 0

        for i in range(0,32):
            newNum= newNum<<1
            if(n&1):
                newNum = newNum|1
            n=n>>1
        return newNum