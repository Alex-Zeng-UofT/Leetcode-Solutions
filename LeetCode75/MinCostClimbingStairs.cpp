#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        
        int i = cost[0], j = cost[1];

        for (int k = 2; k < cost.size(); k++) {
            int step = cost[k] + min(i, j);
            i = j;
            j = step;
        }

        return min(i, j);
    }
};