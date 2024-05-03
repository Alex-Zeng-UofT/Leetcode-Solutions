public class May1st2023 {

    // #213 House Robber II (Dynamic Programming)
    public int rob(int[] nums) {
        return nums.length == 1 ? nums[0] : Math.max(max_amount(nums, 0, nums.length - 1),
                max_amount(nums, 1, nums.length)); // seperate connections on circle and return max
    }

    public int max_amount(int[] nums, int beg, int end) {
        int prev = 0, adj = 0; // prev = nums[i - 2] adj = nums[i - 1]

        for (int i = beg; i < end; i++) {
            int cur = Math.max(prev + nums[i], adj); // determine if we rob or skip

            // update positions
            prev = adj;
            adj = cur;
        }

        return adj; // max amount
    }

    // #55 Jump Game (Greedy)
    public boolean canJump(int[] nums) {
        int end = nums.length - 1; // point we need to reach

        for (int i = end - 1; i >= 0; i--)
            if (nums[i] >= end - i) end = i; // if a i can reach end then we just need to reach i

        return end == 0; // check if we just need to reach the first index
    }

}
