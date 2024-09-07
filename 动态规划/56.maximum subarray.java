package 动态规划;

class Solution {
    public int maxSubArray(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n]; //存储到当前位置最大sum
        dp[0] = nums[0];
        int res = nums[0];
        for(int i=1; i < n; i++) {
            dp[i] = Math.max(nums[i], dp[i-1]+nums[i]);
            if(dp[i] > res) {
                res = dp[i];
            }
        }
        return res;
    }
}
