/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    //brute force with o(N)*2, for each value check if there is a target sum
    int *returnSol = malloc(2 * sizeof(int));
    *returnSize = 2;
    for(int i = 0 ; i <numsSize - 1 ; i++){
        for(int j = i + 1 ; j < numsSize ; j++){
            int sum = nums[i] + nums[j];
            if(sum == target ){
                returnSol[0] = i;
                returnSol[1] = j;
                break;
            }
        }
    }
    return returnSol;
}