class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #if we XOR between 2 identical number will will get 0.
        #so the only number that dont have a twin will stay (0 + 0 + 0) + x = x
        xorsum = 0

        for num in nums:
            xorsum = xorsum ^ num
        return xorsum