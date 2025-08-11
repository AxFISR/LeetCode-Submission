import java.util.*;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        int n = nums.length;

        for (int i = 0; i < n - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue; // skip duplicate i

            // Optional prunings (help on large cases):
            int minSum = nums[i] + nums[i + 1] + nums[i + 2];
            if (minSum > 0) break; // further i will only be larger
            int maxSum = nums[i] + nums[n - 2] + nums[n - 1];
            if (maxSum < 0) continue; // need a bigger i

            int l = i + 1, r = n - 1;
            while (l < r) {
                int sum = nums[i] + nums[l] + nums[r];
                if (sum == 0) {
                    res.add(Arrays.asList(nums[i], nums[l], nums[r]));
                    l++; r--;
                    while (l < r && nums[l] == nums[l - 1]) l++; // skip dup l
                    while (l < r && nums[r] == nums[r + 1]) r--; // skip dup r
                } else if (sum < 0) {
                    l++;
                } else {
                    r--;
                }
            }
        }
        return res;
    }
}
