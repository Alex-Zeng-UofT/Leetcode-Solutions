#include <iostream>
#include <vector>
#include <limits.h>

class Solution {
public:
    bool increasingTriplet(std::vector<int>& nums) {
        int i = INT_MAX;
        int j = INT_MAX;

        for (int n : nums) {
            if (n <= i) i = n;
            else if (n <= j) j = n;
            else return true; 
        }

        return false;
    }
};