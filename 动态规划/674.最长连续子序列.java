package 动态规划;

class Solution {
    public int findLengthOfLCIS(int[] nums) {
        // 1. 动态规划
        // int n = nums.length;
        // int[] dp = new int[n]; //存储到当前位置i最长递增子序列的长度
        // dp[0] = 1;
        // int maxLen = 1;
        // for(int i=1; i < n; i++) {
        //     if(nums[i] > nums[i-1]) {
        //         dp[i] = dp[i-1] +1;
        //     } else {
        //         dp[i] = 1;
        //     }
        //     maxLen = Math.max(maxLen, dp[i]);
        // }
        // return maxLen;
        // 2. 贪心
        int n = nums.length;
        int res = 1;
        int count = 1;
        for(int i=1; i < n; i++) {
            if(nums[i] > nums[i-1]) {
                count++;
            } else {
                count =1;
            }
            res = Math.max(res, count);
        }
        return res;
    }
}