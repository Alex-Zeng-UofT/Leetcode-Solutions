#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        
        int left = 0, right = 0;

        for (int i : nums) right += i;

        for (int i = 0; i < nums.size(); i++) {

            if (i > 0) 
               left += nums[i - 1]; 

            right -= nums[i];

            if (left == right) return i;
        }

        return -1;
    }
};