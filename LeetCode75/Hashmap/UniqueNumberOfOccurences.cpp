#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        
        unordered_map<int, int> map;
        unordered_map<int, int> counter;

        for (int i : arr) map[i]++;

        for (auto i = map.begin(); i != map.end(); i++) {
            counter[i->second]++;
            if (counter[i->second] > 1) return false;
        }
            
        return true;
    }
};