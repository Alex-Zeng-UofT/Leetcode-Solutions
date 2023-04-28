import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Apr28th2023 {

    // #78 Subsets (Backtracking)
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ret = new ArrayList<List<Integer>>(); // initialize return variable
        List<Integer> lst = new ArrayList<Integer>(); // intialize temporary subset

        backtrack(ret, lst, nums, 0); // use recursion to find all subsets

        return ret;
    }

    public void backtrack(List<List<Integer>> ret, List<Integer> lst, int[] nums, int beg) {

        ret.add(new ArrayList<Integer>(lst)); // add this subset to the return list

        for (int i = beg; i < nums.length; i++) { // loop through remaining elements to find subsets
            lst.add(nums[i]); // add new element to current subset to create new subset
            backtrack(ret, lst, nums, i + 1); // find all subsets containing this subset
            lst.remove(lst.size() - 1); // pop element after backtrack for next sub-subset since all subsets are found
        }

        return;
    }

    // #90 Subset II (Backtracking similiar to Subsets I)
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        List<Integer> temp = new ArrayList<Integer>();

        Arrays.sort(nums); // sort array to ensure duplicates are consecutive
        backtrack(ret, temp, nums, 0);

        return ret;
    }

    public void backtrack(List<List<Integer>> ret, List<Integer> temp, int[] nums, int beg) {

        ret.add(new ArrayList<Integer>(temp));

        for (int i = beg; i < nums.length; i++) {

            if (i > beg && nums[i] == nums[i - 1]) continue; // if duplicate is found

            temp.add(nums[i]);
            backtrack(ret, temp, nums, i + 1);
            temp.remove(temp.size() - 1);
        }

        return;
    }
}
