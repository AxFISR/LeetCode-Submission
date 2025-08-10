class Solution {
    public int[] twoSum(int[] nums, int target) {
        //the key is the missing sum, the elem is the index
        HashMap<Integer,Integer> myMap = new HashMap<>();
        int len = nums.length;
        int[] returnArr = new int[2];
        for(int i = 0; i < len ; i++){
            if(myMap.containsKey(target - nums[i])){
                returnArr[0] = i;
                returnArr[1] = myMap.get(target - nums[i]); //the elem is the index
                return returnArr;
            }
            myMap.put(nums[i],i);
        }
        return returnArr;
    }
}