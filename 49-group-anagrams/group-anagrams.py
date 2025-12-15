class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #make a hashmap where the key is a array size 26 counter
        myMap = {}
        returnVal = []
        for val in strs:
            key = [0]*26

            for i in range(len(val)):
                idx = ord(val[i]) - ord('a')
                key[idx]+=1
            key = tuple(key)
            if key in myMap:
                myMap[key].append(val)
            else:
                myMap[key] = []
                myMap[key].append(val)
        return list(myMap.values())
        