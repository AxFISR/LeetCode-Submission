class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        try:
            insertIndex = nums.index(0) #find first zero index
        except ValueError:
            insertIndex = len(nums)
        for skipIndex in range(insertIndex,len(nums)):
            if nums[skipIndex] != 0:
                nums[insertIndex] = nums[skipIndex]
                insertIndex +=1
                nums[skipIndex] = 0
            else:
                continue
        return nums