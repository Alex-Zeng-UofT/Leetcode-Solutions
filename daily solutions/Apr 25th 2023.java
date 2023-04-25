import java.util.LinkedList;
import java.util.Queue;

public class Apr25th2023 {


    // #200 Number of Islands (DFS)
    public void clear(char[][] grid, int row, int col) {
        if (row < 0 || row >= grid.length || col < 0 || col >= grid[0].length ||
                grid[row][col] != '1') // if out of bound or not part of island
            return;

        grid[row][col] = '0'; // delete this section of the island

        // delete the rest of the island using dfs
        clear(grid, row + 1, col);
        clear(grid, row - 1, col);
        clear(grid, row, col + 1);
        clear(grid, row, col - 1);
        return;
    }

    public int numIslands(char[][] grid) {
        int islands = 0; // initialize return variable

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') { // if an island is detected
                    islands++; // increment return variable
                    clear(grid, i, j); // clear this island
                }
            }
        }

        return islands; // done
    }


    // #547 Number of Provinces (BFS)
    public int findCircleNum(int[][] isConnected) {
        int count = 0; // initialize return variable
        boolean[] visited = new boolean[isConnected.length]; // keep track of visited cities

        for (int i = 0; i < isConnected.length; i++) {
            if (!visited[i]) { // if city has not been visited
                count++;
                clearConnections(isConnected, i, visited); // clear all connections to this city
            }
        }

        return count;
    }

    public void clearConnections(int[][] isConnected, int c, boolean[] visited) {
        Queue<Integer> queue = new LinkedList<Integer>(); // FIFO for BFS
        queue.offer(c); // queue city

        while (queue.size() != 0) {
            int city = queue.poll(); // dequeue from queue

            for (int i = 0; i < visited.length; i++) {
                if (isConnected[city][i] == 1 && !visited[i]) { // if "city" is connected with new city i
                    queue.offer(i); // enqueue i
                    visited[i] = true; // city i is now visited
                }
            }
        }
    }
}
