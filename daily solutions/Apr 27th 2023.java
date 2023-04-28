import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class Apr27th2023 {

    // #1091 Shortest Path in Binary Matrix (BFS)
    public int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length, ret = 1; // initialize ret size

        if (n == 1) return grid[0][0] == 1 ? -1 : 1; // if 1x1 matrix
        // base case: either ends == 1 => no possible path
        if (grid[0][0] == 1 || grid[n - 1][n - 1] == 1) return -1;

        // declare shortcut array
        int[] ROWS = {0, -1, -1, -1, 0, 1, 1, 1};
        int[] COLUMNS = {-1, -1, 0, 1, 1, 1, 0, -1};

        int[][] visited = new int[grid.length][grid.length]; // keep track of visited node to prevent overflow
        Queue<int[]> q = new LinkedList<int[]>(); // initialize queue for BFS

        q.offer(new int[]{0, 0}); // enqueue first position in grid

        visited[0][0] = 1; // mark it as visited

        while (!q.isEmpty()) {
            int size = q.size(); // get how many elements in current level

            while (size-- > 0) { // dequeue all these elements
                int[] cur = q.poll();
                int i = cur[0], j = cur[1];

                for (int k = 0; k < 8; k++) {

                    int row = i + ROWS[k]; // new row
                    int col = j + COLUMNS[k]; // new col

                    if ( row >= 0 && row < grid.length && col >= 0 && col < grid[0].length &&
                            grid[row][col] == 0 && visited[row][col] == 0) {

                        if (row == n - 1 && col == n - 1) return ret + 1; // shortest path found

                        q.offer(new int[]{row, col}); // enqueue if not visited and in bound
                        visited[row][col] = 1; // mark as visited
                    }
                }
            }

            ret++; // every level of search => increment in distance
        }

        return -1; // if no such path exists
    }

    // #130 Surrounded Regions (DFS)
    public void solve(char[][] board) {
        int n = board.length, m = board[0].length;

        // clear all regions connected to vertical border
        for (int i = 0; i < n; i++) {
            if (board[i][0] == 'O') clearRegion(board, i, 0);
            if (board[i][m - 1] == 'O') clearRegion(board, i, m - 1);
        }

        // clear all regions connected to horizontal border
        for (int i = 0; i < m; i++) {
            if (board[0][i] == 'O') clearRegion(board, 0, i);
            if (board[n - 1][i] == 'O') clearRegion(board, n - 1, i);
        }

        // restore cleared regions and capture all other regions in matrix
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == 'x') // if region was clear
                    board[i][j] = 'O'; // restore
                else board[i][j] = 'X'; // mark as 'X'
            }
        }
    }


    // helper function using dfs to clear desired region
    public void clearRegion(char[][] board, int row, int col) {
        if (row < 0 || col < 0 || row >= board.length
                || col >= board[0].length || board[row][col] != 'O')
            return;

        board[row][col] = 'x';

        clearRegion(board, row + 1, col);
        clearRegion(board, row - 1, col);
        clearRegion(board, row, col + 1);
        clearRegion(board, row, col - 1);
    }

    // #797 All Paths From Source to Target (DFS)
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        List<Integer> cur = new ArrayList<Integer>(); // initialize current list variable
        List<List<Integer>> ret = new ArrayList<List<Integer>>(); // initialize return variable
        dfs(graph, cur, ret, 0); // add all paths using dfs starting from first node
        return ret;
    }

    public void dfs(int[][] graph, List<Integer> cur, List<List<Integer>> ret, int node) {
        cur.add(node); // add travelled node to current visited

        if (node == graph.length - 1) { // the destination node is reached
            List<Integer> temp = new ArrayList<Integer>(); // create copy variable to avoid entanglement
            temp.addAll(cur); // copy variables from cur
            ret.add(temp); // append this path to our return variable
            return; // nothing left to travel in this path
        }

        for (int i : graph[node]) { // iterate through each child
            dfs(graph, cur, ret, i); // find and add a path from this child
            cur.remove(cur.size() - 1); // remove this child as the path from this child is done
        }

        return;
    }

}
