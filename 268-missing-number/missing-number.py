class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #create identical array but with the missing number, use xor between all to find the missing one
        xor = 0
        for i in range(len(nums)+1):
            xor = i^xor
        for i in range(len(nums)):
            xor = xor^nums[i]
        return xor
        