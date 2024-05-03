import java.util.*;

public class Apr29th2023 {

    // #47 Permutations II (Backtracking)
    public List<List<Integer>> permuteUnique(int[] nums) {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>(); // initialize num : count(num) map
        List<List<Integer>> ret = new ArrayList<List<Integer>>(); // initialize return variable
        List<Integer> temp = new ArrayList<Integer>(); // initialize temp variable

        // map key to its count
        for (int i : nums) {
            if (!map.containsKey(i)) map.put(i, 0);
            map.put(i, map.get(i) + 1);
        }

        backtrack(ret, temp, map, nums.length); // find all permutations using backtracking

        return ret;
    }

    public void backtrack(List<List<Integer>> ret, List<Integer> temp, Map<Integer, Integer> map, int size) {

        if (temp.size() == size) { // len(temp) == len(nums) => all elements add => is a permutation
            ret.add(new ArrayList<Integer>(temp)); // make a copy to avoid entanglement
            return;
        }

        for (int key : map.keySet()) {
            if (map.get(key) != 0) { // if we can add this key to the permutation

                temp.add(key); // add key to temp permutation
                map.put(key, map.get(key) - 1); // decrement its availability

                backtrack(ret, temp, map, size); // recurse and expand permutation

                map.put(key, map.get(key) + 1); // restore availability
                temp.remove(temp.size() - 1); // pop from temp permutation
            }
        }
    }

    // #39 Combination Sum (Backtracking)
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> ret = new ArrayList<List<Integer>>(); // return variable
        List<Integer> temp = new ArrayList<Integer>(); // temp combination sum

        backtrack(ret, temp, target, candidates, 0); // find all combination sums using backtracking

        return ret;
    }

    public void backtrack(List<List<Integer>> ret, List<Integer> temp, int target, int[] nums, int beg) {
        if (target == 0) { // if target is reached
            ret.add(new ArrayList<Integer>(temp)); // add copy of combination sum
            return;
        }

        for (int i = beg; i < nums.length; i++) {
            if (nums[i] <= target) { // if potential combination sum
                temp.add(nums[i]); // add element to temp combination sum

                backtrack(ret, temp, target - nums[i], nums, i); // backtrack to find remainder sum

                temp.remove(temp.size() - 1); // pop element and move on to next
            }
        }
    }

    // #40 Combination Sum II
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> ret = new ArrayList<List<Integer>>(); // ret variable
        List<Integer> temp = new ArrayList<Integer>(); // temporary combination sum
        Arrays.sort(candidates); // sort to ensure all duplicates are consecutive

        backtrack(ret, temp, candidates, target, 0); // backtrack to find all combination sums

        return ret;
    }

    public void backtrack(List<List<Integer>> ret, List<Integer> temp, int[] nums, int target, int beg) {
        if (target == 0) { // if we reached the target
            ret.add(new ArrayList<Integer>(temp)); // add copy of the combination sum
            return;
        }

        for (int i = beg; i < nums.length; i++) {
            if (i > beg && nums[i] == nums[i - 1]) continue; // skip if duplication

            if (nums[i] <= target) { // if nums[i] is a potential candidate
                temp.add(nums[i]); // add to temp list

                backtrack(ret, temp, nums, target - nums[i], i + 1); // backtrack to complete new target

                temp.remove(temp.size() - 1); // pop from temp list
            }
            else break; // nums[i] > target => nums[k] > target for all k >= i
        }
    }

}
