#include <bits/stdc++.h>
using namespace std;


class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        
        int count = 0;
        unordered_map<int, int> mp;

        for (int i : nums) 
            mp[i]++;

        for (int i : nums) {
            
            if (2*i == k) 
                count += mp[i]/2;
            else count += min(mp[i], mp[k - i]);

            mp[i] = 0;
        }

        return count;
    }
};