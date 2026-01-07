class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0]
        for i in range(1,n+1):
            cnt=0
            bit = i
            while(bit):
                if(1&bit):
                    cnt+=1
                bit = bit>>1
            ans.append(cnt)
        return ans
