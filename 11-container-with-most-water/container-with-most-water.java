class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int maxSol = 0;
        while(left < right){
            int temp;
            if(height[left] <= height[right]){
                temp = height[left]*(right-left);
                left++;
            }
            else{
                temp = height[right]*(right-left);
                right--;
            }
            if(temp > maxSol){
                maxSol = temp;
            }

        }
        return maxSol;
    }
}