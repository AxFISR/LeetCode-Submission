class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dupeMap = {}

        for num in nums:
            if dupeMap.get(num,0):
                return True
            dupeMap[num] = 1
        return False
        