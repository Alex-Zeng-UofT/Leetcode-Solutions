#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int largestAltitude(vector<int>& gain) {

        int m = 0;
        int cur = 0;

        for (int i : gain) {
            cur += i;
            m = max(cur, m);
        }

        return m;
    }
};