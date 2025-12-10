class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        "make hashtable where the the key is target-nums[i] and value is the index "
        "if target-nums[i] dosent exist , insert nums[i] to hashtable"
        my_dict = {}
        solution = [0,0]
        for i in range(len(nums)):
            if target-nums[i] in my_dict:
                solution[0] = i
                solution[1] = my_dict[(target-nums[i])]
                return solution
            else:
                my_dict[nums[i]] = i
        return solution
