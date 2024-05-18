#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {

        if (nums.size() == 3) return max(nums[0] + nums[2], nums[1]);
        if (nums.size() == 2) return max(nums[0], nums[1]);
        if (nums.size() == 1) return nums[0];

        int i = nums[0];
        int j = nums[1];
        int k = i + nums[2];

        for (int p = 3; p < nums.size(); p++) {
            int profit = nums[p] + max(i, j);
            i = j;
            j = k;
            k = profit;
        }

        return max(j, k);
    }
};