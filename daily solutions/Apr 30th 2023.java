import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Apr30th2023 {

    // #17 Letter Combinations of a Phone Number (Backtracking)
    public List<String> letterCombinations(String digits) {
        List<String> ret = new ArrayList<String>(); // initialize return variable

        if (digits.length() == 0) return ret; // if empty digits string

        // initialize map from each number to its set of letters
        HashMap<Character, String> map = new HashMap<Character, String>();
        map.put('2', "abc");
        map.put('3', "def");
        map.put('4', "ghi");
        map.put('5', "jkl");
        map.put('6', "mno");
        map.put('7', "pqrs");
        map.put('8', "tuv");
        map.put('9', "wxyz");

        char[] s = new char[digits.length()]; // use char arrays for efficiency

        backtrack(ret, s, 0, map, 0, digits); // use backtracking to find all combinations

        return ret;
    }

    public void backtrack(List<String> ret, char[] s, int len, Map<Character, String> map, int num, String digit) {

        if (len == digit.length()) { // if length of array is the same as the length of digits
            ret.add(new String(s)); // add the array converted to a string
            return;
        }

        String candidates = map.get(digit.charAt(num)); // set of possible letters

        for (int i = 0; i < candidates.length(); i++) { // explore all possible letters
            s[len++] = candidates.charAt(i);
            backtrack(ret, s, len--, map, num + 1, digit); // recurse and check next number in digits
        }
    }

    // #22 Generate Parentheses (Backtracking)
    public List<String> generateParenthesis(int n) {
        List<String> ret = new ArrayList<String>(); // initialize return variable
        char[] s = new char[n * 2]; // use char array instead of strings for efficiency

        backtrack(ret, s, 0, 0, 0, n); // fing all combinations using backtracking

        return ret;
    }

    public void backtrack(List<String> ret, char[] s, int len, int open, int closed, int n) {

        // when we used all sets of parentheses
        if (open == n && closed == n) {
            ret.add(new String(s));
            return;
        }

        // '(' in stock => can apply '('
        if (open < n) {
            s[len++] = '(';
            backtrack(ret, s, len--, open + 1, closed, n);
        }

        // num of ')' < num of '(' => can apply ')'
        if (closed < open) {
            s[len++] = ')';
            backtrack(ret, s, len--, open, closed + 1, n);
        }
    }

    // #79 Word Search (Backtracking/DFS)
    public boolean exist(char[][] board, String word) {
        boolean[][] visited = new boolean[board.length][board[0].length]; // keep track of visited

        for (int i = 0; i < board.length; i++)
            for (int j = 0; j < board[0].length; j++)
                if (dfs(board, word, 0, i, j, visited)) return true; // word is found

        return false;
    }

    public boolean dfs(char[][] board, String word, int idx, int row, int col, boolean[][] visited) {
        if (row < 0 || col < 0 || row >= board.length || col >= board[0].length
                || idx >= word.length() || board[row][col] != word.charAt(idx) || visited[row][col])
            return false; // out of bounds or invalid letter or already visited

        if (idx == word.length() - 1) return true; // if last letter of word is found

        visited[row][col] = true; // mark as visited for dfs

        if (dfs(board, word, idx + 1, row + 1, col, visited)
                || dfs(board, word, idx + 1, row - 1, col, visited)
                || dfs(board, word, idx + 1, row, col + 1, visited)
                || dfs(board, word, idx + 1, row, col - 1, visited))
            return true; // word is found

        visited[row][col] = false; // unmark as visited if word not found
        return false;
    }

}
