#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int equalPairs(vector<vector<int>>& grid) {
        
        unordered_map<string, int> counter1;
        unordered_map<string, int> counter2;

        int n = grid[0].size();
        int pairs = 0;

        for (int i = 0; i < n; i++) {
            string sequence1 = "";
            string sequence2 = "";
            for (int j = 0; j < n; j++) {
                sequence1 += to_string(grid[i][j]) + ' ';
                sequence2 += to_string(grid[j][i]) + ' ';
            }
            counter1[sequence1]++;
            counter2[sequence2]++;
        }

        for (auto p = counter1.begin(); p != counter1.end(); p++) {
            pairs += counter2[p->first] * p->second;
        }

        return pairs;
    }
};