public class May2nd2023 {

    // #45 Jump Game II
    public int jump(int[] nums) {
        int jumps = 0; // initialize return variable
        int left = 0, right = 0; // window for each jump

        while (right < nums.length - 1) { // while we haven't reached the end

            int max = 0;

            // find furthest point from jumps
            for (int i = left; i <= right; i++) {
                int cur = nums[i] + i;
                if (cur > max) max = cur;
            }

            left = right + 1; // new left is the next of right pointer
            right = max; // new right is the furthest point of jump

            jumps++; // increment jumps
        }

        return jumps;
    }

    // #62 Unique Paths (Dynamic Programming)
    public int uniquePaths(int m, int n) {
        int[][] grid = new int[m][n]; // initialize variable to store data
        return paths(grid, 0, 0, m, n);
    }

    public int paths(int[][] grid, int i, int j, int m, int n) {
        if (i >= m || j >= n) // out of bounds
            return 0;

        if (i == m - 1 && j == n - 1) // reached destination
            return 1;

        if (grid[i][j] != 0) // previously already calculated
            return grid[i][j];

        // calculate how many path from this point
        grid[i][j] = paths(grid, i + 1, j, m, n) + paths(grid, i, j + 1, m, n);

        return grid[i][j];
    }

}
