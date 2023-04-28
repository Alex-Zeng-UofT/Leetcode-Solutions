import java.util.LinkedList;
import java.util.Queue;

public class Apr27th2023 {

    public int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length, ret = 1;

        if (grid[0][0] == 1 || grid[n - 1][n - 1] == 1) return -1;

        int[] ROWS = {0, -1, -1, -1, 0, 1, 1, 1};
        int[] COLUMNS = {-1, -1, 0, 1, 1, 1, 0, -1};

        int[][] visited = new int[grid.length][grid.length];
        Queue<int[]> q = new LinkedList<int[]>();

        q.offer(new int[]{0, 0});

        visited[0][0] = 1;

        while (!q.isEmpty()) {
            int size = q.size();
            while (size-- > 0) {
                int[] cur = q.poll();
                int i = cur[0], j = cur[1];

                if (i == n - 1 && j == n - 1) return ret;

                for (int k = 0; k < 8; k++) {
                    int row = i + ROWS[k];
                    int col = j + COLUMNS[k];
                    if ( row >= 0 && row < grid.length &&
                            col >= 0 && col < grid[0].length &&
                            grid[row][col] == 0 && visited[row][col] == 0) {

                        if (row == n - 1 && col == n - 1) return ret + 1;

                        q.offer(new int[]{row, col});
                        visited[row][col] = 1;
                    }
                }
            }
            ret++;
        }

        return -1;
    }

}
