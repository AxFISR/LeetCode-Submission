class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer,Integer> myMap = new HashMap<>();
        int len = nums.length;

        for(int i = 0 ; i < len ; i++){
            if(myMap.containsKey(nums[i])){
                int count = myMap.get(nums[i]); 
                myMap.put(nums[i], count + 1);

            }
            else{
                myMap.put(nums[i], 1 );
            }
        }

        int[] returnVal = new int[k];
        int index = 0;
        for(int j = 0 ; j < k ; j++){
                int maxVal = 0;
                int maxKey = 0;
                for (Integer key : myMap.keySet()) {
                    int value = myMap.get(key);
                    if(value > maxVal){
                        maxVal = value;
                        maxKey = key;
                    }
                    
                }
                returnVal[index] = maxKey;
                index++;
                myMap.remove(maxKey);
        }
        return returnVal;


    }
}