class Solution {
    public int[] twoSum(int[] numbers, int target) {
        //two pointers, if sum is big, move right down. if its small move left up

        int leftP = 0;
        int rightP = numbers.length -1;
        int[] returnVal = new int[2];
        while(leftP < rightP){
            int sum = numbers[leftP] + numbers[rightP];
            if(sum == target ){
                returnVal[0] = leftP+1;
                returnVal[1] = rightP+1;
                return returnVal;
            }
            if(sum > target){
                rightP--;
            }
            else{
                leftP++;
            }
        } 
        return returnVal;
    }
}