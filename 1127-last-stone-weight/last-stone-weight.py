class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        while(len(stones) > 1):
            max1 = max(stones)
            stones.remove(max1)
            max2 = max(stones)
            if(max1 == max2):
                stones.remove(max2)
            else:
                idx = stones.index(max2)
                stones[idx] = max1 - max2
        if(not len(stones)):
            return 0
        return stones[0]