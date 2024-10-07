#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        
        int beg = 0;
        int m = 0;
        int zeros = 1;

        for (int i = 0; i < nums.size(); i++) {
            
            if (nums[i] == 0) zeros--;

            while (zeros < 0) 
                if (nums[beg++] == 0) zeros++;

            m = max(m, i - beg);
        }

        return m;
    }
};