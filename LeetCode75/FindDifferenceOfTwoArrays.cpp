#include <iostream>
#include <vector>
#include <unordered_map>    
using namespace std;

class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        
        unordered_map<int, int> one;
        unordered_map<int, int> two;

        vector<vector<int>> bruh;

        vector<int> first;
        vector<int> second;

        for (int i : nums1) one[i]++;
        for (int i : nums2) two[i]++;

        for (auto p = one.begin(); p != one.end(); p++) {
            if (!two[p->first]) first.push_back(p->first);
        }

        for (auto p = two.begin(); p != two.end(); p++) {
            if (!one[p->first]) second.push_back(p->first);
        }

        bruh.push_back(first);
        bruh.push_back(second);

        return bruh;
    }
};