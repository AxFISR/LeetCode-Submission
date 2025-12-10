class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        myMap = {}
        for value in (nums):
            if value in myMap:
                return True
            myMap[value] = True
        return False
        