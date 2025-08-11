class Solution {
    private int addIfBelow(int h, int bound) {
        return bound > h ? bound - h : 0;
    }

    public int trap(int[] height) {
        int n = height.length;
        if (n < 3) return 0;

        int left = 0, right = n - 1;
        int leftMax = 0, rightMax = 0;
        int total = 0;

        while (left < right) {
            if (height[left] < height[right]) {        // process left side
                leftMax = Math.max(leftMax, height[left]);
                total += addIfBelow(height[left], leftMax);
                left++;
            } else {                                    // process right side
                rightMax = Math.max(rightMax, height[right]);
                total += addIfBelow(height[right], rightMax);
                right--;
            }
        }
        return total;
    }
}
