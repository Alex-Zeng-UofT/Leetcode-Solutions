import java.util.Arrays;

public class May6th2023 {

    // #1143 Longest Common Subsequence (DP)
    public int longestCommonSubsequence(String text1, String text2) {
        int n = text1.length(), m = text2.length(); // constants
        int[][] grid = new int[n + 1][m + 1]; // dp grid

        char[] one = text1.toCharArray(), two = text2.toCharArray(); // char array for efficiency

        // bottom up solution
        for (int i = n - 1; i >= 0; i--) {
            for (int j = m - 1; j >= 0; j--) {
                if (one[i] == two[j]) // same character
                    grid[i][j] = 1 + grid[i + 1][j + 1];
                else // different // character
                    grid[i][j] = Math.max(grid[i + 1][j], grid[i][j + 1]);
            }
        }

        return grid[0][0];
    }

    // #583 Delete Operation for Two Strings (DP)
    public int minDistance(String word1, String word2) {
        int n = word1.length(), m = word2.length();
        int[][] grid = new int[n + 1][m + 1];
        char[] one = word1.toCharArray(), two = word2.toCharArray();

        for (int i = n - 1; i >= 0; i--) {
            for (int j = m - 1; j >= 0; j--) {
                if (one[i] == two[j])
                    grid[i][j] = 1 + grid[i + 1][j + 1];
                else
                    grid[i][j] = Math.max(grid[i + 1][j], grid[i][j + 1]);
            }
        }

        // find longest common subsequence then remove the extras in both strings
        return n + m - 2 * grid[0][0];
    }

    // #1498 Number of Subsequences That Satisfy the Given Sum Condition (Two Pointers)
    public int numSubseq(int[] nums, int target) {
        Arrays.sort(nums);

        int mod = 1000000007, count = 0;
        int[] power = new int[nums.length];
        power[0] = 1;

        for (int i = 1; i < nums.length; i++)
            power[i] = (power[i - 1] * 2) % mod;

        int left = 0, right = nums.length - 1;

        while (left <= right) {
            if (nums[left] + nums[right] <= target) {
                count += power[right - left];
                count %= mod;
                left++;
            }
            else right--;
        }
        return count;
    }

}
