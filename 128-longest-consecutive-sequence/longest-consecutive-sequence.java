class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> mySet = new HashSet<>();
        //put all numbers in set to remove duplicates
        for(int i = 0 ; i < nums.length ; i++){
            if(!mySet.contains(nums[i])){
                mySet.add(nums[i]);
            }
        }

        int longestC = 0;
        for(Integer value : mySet){
            int checker = 0;
            if(!mySet.contains(value - 1)){
                while(mySet.contains(value)){
                    checker++;
                    value++;
                }
                
            }
            if (checker > longestC){
                longestC = checker;
            }
        }
        return longestC;
    }
}