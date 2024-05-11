#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {

        int m = 0;
        int beg = 0;

        for (int i = 0; i < nums.size(); i++) {

            if (nums[i] == 0) k--;

            while (k < 0) {
                if (nums[beg++] == 0) k++;
            }

            m = max(m, i - beg + 1);
        }

        return m;
    }
};