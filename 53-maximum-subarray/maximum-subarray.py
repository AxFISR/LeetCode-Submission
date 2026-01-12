class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # current_sum = הסכום הכי טוב שמסתיים באינדקס הנוכחי
        current_sum = nums[0]

        # max_sum = הסכום הכי טוב שראינו עד עכשיו
        max_sum = nums[0]

        for i in range(1, len(nums)):
            # או ממשיכים את התת-מערך הקיים
            # או מתחילים תת-מערך חדש מהאיבר הנוכחי
            current_sum = max(nums[i], current_sum + nums[i])

            # מעדכנים מקסימום גלובלי
            max_sum = max(max_sum, current_sum)

        return max_sum
